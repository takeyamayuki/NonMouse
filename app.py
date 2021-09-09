import cv2
import mediapipe as mp
import numpy as np
import time
import tkinter as tk
from pynput.mouse import Button, Controller
mouse = Controller()
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


def tk_arg():
    root = tk.Tk()
    root.title(u"First Setup")
    root.geometry("280x280")
    Val1 = tk.IntVar()
    Val2 = tk.IntVar()
    Val3 = tk.IntVar()
    Val4 = tk.IntVar()
    Val4.set(30)                            # デフォルトマウス感度
    Mode = ['Gesture', 'Mouse', 'Touch']
    # Camera
    Static1 = tk.Label(text=u'Camera').grid(row=1)
    for i in range(3):
        tk.Radiobutton(root,
                       value=i,
                       variable=Val1,
                       text='Device{}'.format(i)
                       ).grid(row=2, column=i*2)
    St1 = tk.Label(text=u'     ').grid(row=3)
    # Sensitivity
    Static4 = tk.Label(text=u'Sensitivity').grid(row=4)
    s1 = tk.Scale(root, orient='h',
                  from_=1, to=100, variable=Val4
                  ).grid(row=5, column=2)
    St4 = tk.Label(text=u'     ').grid(row=6)
    # Mode
    Static2 = tk.Label(text=u'Mode').grid(row=7)
    for j in range(3):
        tk.Radiobutton(root,
                       value=j,
                       variable=Val2,
                       text=Mode[j]
                       ).grid(row=8, column=j*2)
    St2 = tk.Label(text=u'     ').grid(row=9)
    # continue
    Button = tk.Button(text="continue", command=root.quit).grid(
        row=10, column=2)
    # 待機
    root.mainloop()
    # 出力
    cap_device = Val1.get()       # 0,1,2
    mode = Val2.get()             # 0:Gesture 1:Mouse 2:Touch
    kando = Val4.get()/10         # 1~10
    return cap_device, mode, kando


def main():              
    dis = 0.7               # くっつける距離の定義
    preX, preY = 0, 0
    nowCli, preCli = 0, 0   # 現在、前回の左クリック状態
    norCli, prrCli = 0, 0   # 現在、前回の右クリック状態
    douCli = 0
    LiTx = []
    LiTy = []
    i, k = 0, 0
    cap_width=1280
    cap_height=720
    start, c_start = float('inf'), float('inf')
    cap_device, mode, kando = tk_arg()  # tkinterで引数をgui化
    cap = cv2.VideoCapture(cap_device)  # Webカメラ入力
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, cap_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cap_height)
    cfps=str(int(cap.get(cv2.CAP_PROP_FPS)))
    if cfps == '60':
        ran=6              # スムージング量（小さい:カーソルが小刻みに動く 大きい:遅延が大）
    else:
        ran=3
    hands = mp_hands.Hands(
        min_detection_confidence=0.7,   # 検出信頼度
        min_tracking_confidence=0.7,    # 追跡信頼度
        max_num_hands=1                 # 最大検出数
    )
    print(ran)
    # メインループ
    while cap.isOpened():
        p_s = time.perf_counter()
        success, image = cap.read()
        if not success:
            continue
        if mode == 1:                   # Mouse
            image = cv2.flip(image, 0)  # 上下反転
        elif mode == 2:                 # Touch
            image = cv2.flip(image, 1)  # 左右反転

        # 画像を水平方向に反転し、BGR画像をRGBに変換
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        image.flags.writeable = False   # 参照渡しのためにイメージを書き込み不可としてマーク
        results = hands.process(image)
        image.flags.writeable = True    # 画像に手のアノテーションを描画
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        image_height, image_width, _ = image.shape

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # preX, preY, LiTx, LiTyの初期値に現在のマウス位置を代入 1回だけ実行
            if i == 0:
                preX = hand_landmarks.landmark[8].x
                preY = hand_landmarks.landmark[8].y
                for j in range(ran):
                    LiTx.append(hand_landmarks.landmark[8].x)
                    LiTy.append(hand_landmarks.landmark[8].y)
                i = +1

            # 指相対座標の基準距離、以後mediapipeから得られた距離をこの値で割る
            Kij = (hand_landmarks.landmark[0].x - hand_landmarks.landmark[1].x,
                   hand_landmarks.landmark[0].y - hand_landmarks.landmark[1].y)
            absKij = np.linalg.norm(Kij)
            # print('hand_landmarks:', hand_landmarks.landmark[8].x)
            # 人差し指の先端と中指の先端間のユークリッド距離
            Ugo = (hand_landmarks.landmark[8].x - hand_landmarks.landmark[12].x,
                   hand_landmarks.landmark[8].y - hand_landmarks.landmark[12].y)
            absUgo = np.linalg.norm(Ugo)/absKij
            # print("absUgo:",absUgo)
            # 人差し指の第２関節と親指の先端間のユークリッド距離
            Cli = (hand_landmarks.landmark[6].x - hand_landmarks.landmark[4].x,
                   hand_landmarks.landmark[6].y - hand_landmarks.landmark[4].y)
            absCli = np.linalg.norm(Cli)/absKij
            # print("absCli:",absCli)

            # 人差し指の先端をカーソルに対応 && ３つ平均でスムージング
            # 末尾に追加
            LiTx.append(hand_landmarks.landmark[8].x)
            LiTy.append(hand_landmarks.landmark[8].y)
            if len(LiTx) > ran:
                LiTx.pop(0)         # 先頭を削除
                LiTy.pop(0)
            # カメラ座標をマウス移動量に変換        平均化：image_width掛ける前に平均化するべきでは？ 
            dx = kando * (sum(LiTx)/ran - preX) * image_width
            dy = kando * (sum(LiTy)/ran - preY) * image_height
            
            # フラグ
            # click状態
            if absCli < dis:
                nowCli = 1          # nowCli:左クリック状態(1:click  0:non click)
                cv2.circle(image, (int(hand_landmarks.landmark[8].x * image_width), int(
                    hand_landmarks.landmark[8].y * image_height)), 20, (0, 250, 250), thickness=5, lineType=cv2.LINE_8, shift=0)
            elif absCli >= dis:
                nowCli = 0
            if np.abs(dx) > 5 and np.abs(dy) > 5:
                k = 0                           # 「動いている」ときk=0
            # 右クリック状態 １秒以上クリック状態&&カーソルを動かさない
            # 「動いていない」ときでクリックされたとき
            if nowCli == 1 and np.abs(dx) < 5 and np.abs(dy) < 5:
                if k == 0:          # k:クリック状態&&カーソルを動かしてない。113, 140行目でk=0にする
                    start = time.perf_counter()
                    k += 1
                end = time.perf_counter()
                if end-start > 1:
                    norCli = 1
                    cv2.circle(image, (int(hand_landmarks.landmark[8].x * image_width), int(
                    hand_landmarks.landmark[8].y * image_height)), 20, (0, 0, 250), thickness=5, lineType=cv2.LINE_8, shift=0)
            else:
                norCli = 0
            # print("np.abs(dx)", np.abs(dx))

            # 動かす
            # cursor
            if absUgo >= dis:
                mouse.move(dx, dy)
                cv2.circle(image, (int(hand_landmarks.landmark[8].x * image_width), int(
                    hand_landmarks.landmark[8].y * image_height)), 8, (250, 0, 0), thickness=5, lineType=cv2.LINE_8, shift=0)
            # left click
            if nowCli == 1 and nowCli != preCli:
                mouse.press(Button.left)
                # print('Click')
            # left click release
            if nowCli == 0 and nowCli != preCli:
                mouse.release(Button.left)
                k = 0
                # print('Release')
                if douCli == 0:                             # 1回目のクリックが終わったら、時間測る
                    c_start = time.perf_counter()
                    douCli += 1
                c_end = time.perf_counter()
                if 10*(c_end-c_start) > 5 and douCli == 1:  # 0.5秒以内にもう一回クリックしたらダブルクリック
                    mouse.click(Button.left, 2)             # double click
                    douCli = 0
            # right click
            if norCli == 1 and norCli != prrCli:
                mouse.release(Button.left)                  # 何故か必要
                mouse.press(Button.right)
                mouse.release(Button.right)
                # print("right click")
            # scroll
            if hand_landmarks.landmark[8].y-hand_landmarks.landmark[5].y > -0.06:
                mouse.scroll(0, -dy/6)     # スクロール感度:1/6にする

            preX = sum(LiTx)/ran
            preY = sum(LiTy)/ran
            preCli = nowCli
            prrCli = norCli

        p_e = time.perf_counter()
        fps = str(int(1/(float(p_e)-float(p_s))))
        cv2.putText(image, "camFPS:"+cfps,
                    (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
        cv2.putText(image, "FPS:"+fps, (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

        cv2.imshow('NonMouse', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break
    cap.release()


if __name__ == "__main__":
    main()
