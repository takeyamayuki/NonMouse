import argparse
import cv2
import mediapipe as mp
import numpy as np
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
    preCli = 0
    douCli = 0
    LiTx = []
    LiTy = []
    i=0
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
                if i==0:
                    preX=hand_landmarks.landmark[8].x * image_width
                    preY=hand_landmarks.landmark[8].y * image_height
                    for j in range(ran):
                        LiTx.append(hand_landmarks.landmark[8].x * image_width)
                        LiTy.append(hand_landmarks.landmark[8].y * image_height)
                    i=+1

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

                # click状態
                if absCli < dis:
                    nowCli = 1
                if absCli >= dis:
                    nowCli = 0

                # マウス動かす
                if absUgo >= dis:
                    if args.direction == 0:
                        mouse.move(dx, -dy)
                    if args.direction == 1:
                        mouse.move(dx, dy)
                # click
                if nowCli == 1 and nowCli != preCli:
                    mouse.press(Button.left)
                    douCli += 1
                    print('Click')
                # release
                if nowCli == 0 and nowCli != preCli:
                    mouse.release(Button.left)
                    douCli += 1
                    print('Release')

                preX = sum(LiTx)/ran
                preY = sum(LiTy)/ran
                preCli = nowCli

        cv2.imshow('NonMouse', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break
    cap.release()


if __name__ == "__main__":
    main()
