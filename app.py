import argparse
import cv2
import mediapipe as mp
import numpy as np
import time
from numpy.testing._private.utils import jiffies
from pynput.mouse import Button, Controller
mouse = Controller()
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands


def main():
    # マウス感度（大きくすると、小刻みに動きやすくなるので、同時にranも大きくする）
    kando = 1.5
    # スムージング量（小さいとカーソルが小刻みに動きやすくなるが、大きいと遅延が大きくなる）
    ran = 3
    # タッチ距離（遠いほど小さく、近いほど大きい値にする）
    dis = 65
    preX, preY = 0, 0
    nowCli, preCli = 0, 0      # 現在、前回の左クリック状態
    norCli, prrCli = 0, 0      # 現在、前回の右クリック状態
    douCli = 0
    LiTx = []
    LiTy = []
    i, k, h = 0, 0, 0
    start , c_start = float('inf'), float('inf')
    # 引数
    parser = argparse.ArgumentParser()
    parser.add_argument("--device", type=int, default=0)
    parser.add_argument("--direction", type=int, default=0)
    parser.add_argument("--distance", type=int, default=65)
    parser.add_argument("--kando", type=float, default=1.5)
    args = parser.parse_args()
    cap_device = args.device
    dis = args.distance
    kando = args.kando
    # Webカメラ入力
    cap = cv2.VideoCapture(cap_device)

    hands = mp_hands.Hands(
        min_detection_confidence=0.7,   # 検出信頼度
        min_tracking_confidence=0.7,    # 追跡信頼度
        max_num_hands=1                 # 最大検出数
    )

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            continue
        # 画像を水平方向に反転し、BGR画像をRGBに変換
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        # 参照渡しのためにイメージを書き込み不可としてマーク
        image.flags.writeable = False
        results = hands.process(image)
        # 画像に手のアノテーションを描画
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        image_height, image_width, _ = image.shape

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # preX, preY, LiTx, LiTyの初期値に現在のマウス位置を代入 1回だけ実行
                if i == 0:
                    preX = hand_landmarks.landmark[8].x * image_width
                    preY = hand_landmarks.landmark[8].y * image_height
                    for j in range(ran):
                        LiTx.append(hand_landmarks.landmark[8].x * image_width)
                        LiTy.append(
                            hand_landmarks.landmark[8].y * image_height)
                    i = +1

                # print('hand_landmarks:', hand_landmarks.landmark[8].x)
                # 人差し指の先端と中指の先端間のユークリッド距離
                Ugo = (hand_landmarks.landmark[8].x * image_width - hand_landmarks.landmark[12].x * image_width,
                       hand_landmarks.landmark[8].y * image_height - hand_landmarks.landmark[12].y * image_height)
                absUgo = np.linalg.norm(Ugo)
                # 人差し指の第２関節と親指の先端間のユークリッド距離
                Cli = (hand_landmarks.landmark[6].x * image_width - hand_landmarks.landmark[4].x * image_width,
                       hand_landmarks.landmark[6].y * image_height - hand_landmarks.landmark[4].y * image_height)
                absCli = np.linalg.norm(Cli)
                # 中指の先端と薬指の先端間のユークリッド距離
                Scr = (hand_landmarks.landmark[12].x * image_width - hand_landmarks.landmark[16].x * image_width,
                       hand_landmarks.landmark[12].y * image_height - hand_landmarks.landmark[16].y * image_height)
                absScr = np.linalg.norm(Scr)

                # 移動量平均によるスムージング
                # 末尾に追加
                LiTx.append(hand_landmarks.landmark[8].x * image_width)
                LiTy.append(hand_landmarks.landmark[8].y * image_height)
                if len(LiTx) > ran:
                    LiTx.pop(0)     # 先頭を削除
                    LiTy.pop(0)
                # カメラ座標をマウス移動量に変換
                dx = kando * (sum(LiTx)/ran - preX)
                dy = kando * (sum(LiTy)/ran - preY)

                # フラグ
                # click状態
                if absCli < dis:
                    nowCli = 1                                  # nowCli:左クリック状態(1:click  0:non click)
                if absCli >= dis:
                    nowCli = 0
                # # スクロール状態
                if absScr < dis:
                    nowScr = 1                                  # norCli:右クリック状態(1:click  0:non click)
                if absScr >= dis:
                    nowScr = 0
                if np.abs(dx) > 5 and np.abs(dy) > 5:
                    k = 0
                # 右クリック状態 １秒以上クリック状態&&カーソルを動かさない
                if nowCli == 1 and np.abs(dx) < 5 and np.abs(dy) < 5:
                    if k == 0:                                  # k:クリック状態&&カーソルを動かしてない
                        start = time.perf_counter()
                        k += 1
                    end = time.perf_counter()
                    if end-start > 1:
                        norCli = 1
                else:
                    norCli = 0
                
                # 動かす
                # cursor
                if absUgo >= dis:
                    if args.direction == 0:
                        mouse.move(dx, -dy)
                        # print(dx, -dy)
                    if args.direction == 1:
                        mouse.move(dx, dy)
                # left click
                if nowCli == 1 and nowCli != preCli:
                    mouse.press(Button.left)
                    douCli += 1
                    cstart = time.perf_counter
                    print('Click')
                # left click release
                if nowCli == 0 and nowCli != preCli:
                    mouse.release(Button.left)
                    k = 0
                    print('Release')
                    if douCli == 0:                             # 一回目のクリックが終わったら、時間測る
                        c_start = time.perf_counter()
                        douCli += 1
                    c_end = time.perf_counter()
                    if 10*(c_end-c_start) > 5 and douCli == 1:  # 0.5秒以内にもう一回クリックしたらdouCli=2にする
                        douCli = 2
                # double click
                if douCli == 2:
                    mouse.click(Button.left, 2)
                    douCli = 0
                # right click
                if norCli == 1 and norCli != prrCli:
                    mouse.release(Button.left)
                    mouse.press(Button.right)
                    mouse.release(Button.right)
                    print("right click")
                # scroll
                if nowScr == 1:
                    mouse.scroll(0, dy/1.5)
                    print("scroll")

                preX = sum(LiTx)/ran
                preY = sum(LiTy)/ran
                preCli = nowCli
                prrCli = norCli

        cv2.imshow('NonMouse', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break
    cap.release()


if __name__ == "__main__":
    main()
