import cv2
import mediapipe as mp
import numpy as np
from pynput.mouse import Button, Controller
mouse = Controller()
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

kando = 1.5                   # マウス感度
preX, preY = 0, 0
preCli = 0
douCli = 0
ran = 5                     # スムージング量
LiTx = [0, 0, 0, 0, 0]
LiTy = [0, 0, 0, 0, 0]
dis = 65                    # タッチ距離

# Webカメラ入力
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

with mp_hands.Hands(
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7,
        max_num_hands=1) as hands:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            # ビデオをロードする場合は、「continue」ではなく「break」を使用してください
            continue

        # 後で自分撮りビューを表示するために画像を水平方向に反転し、BGR画像をRGBに変換
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        # パフォーマンスを向上させるために、オプションで、参照渡しのためにイメージを書き込み不可としてマーク
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
                #print('hand_landmarks:', hand_landmarks)
                '''
                print(
                    f'人差し指の先端: (',
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x}, '
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y})'
                )
                print(
                    f'中指の先端: (',
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x}, '
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y})'
                )
                print(
                    f'親指の先端: (',
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x}, '
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y})'
                )
                print(
                    f'人差し指の第２関節: (',
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].x}, '
                    f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y})'
                )
                '''
                # 人差し指の先端と中指の先端間のユークリッド距離
                Ugo = (hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width -
                       hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x * image_width,
                       hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height -
                       hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * image_height)
                absUgo = np.linalg.norm(Ugo)
                # 人差し指の第２関節と親指の先端間のユークリッド距離
                Cli = (hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].x * image_width -
                       hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x * image_width,
                       hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y * image_height -
                       hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].y * image_height)
                absCli = np.linalg.norm(Cli)
                # 移動量平均によるスムージング
                # 末尾に追加
                LiTx.append(
                    hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width)
                LiTy.append(
                    hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height)
                if len(LiTx) > ran:
                    # 先頭を削除
                    LiTx.pop(0)
                    LiTy.pop(0)
                # カメラ座標をマウス移動量に変換
                dx = kando * (sum(LiTx)/len(LiTx) - preX)
                dy = kando * (sum(LiTy)/len(LiTy) - preY)
                # click状態
                if absCli < dis:
                    nowCli = 1
                if absCli >= dis:
                    nowCli = 0

                # マウス動かす
                if absUgo >= dis:
                    mouse.move(dx, -dy)
                    # print('Move')
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

                preX = sum(LiTx)/len(LiTx)
                preY = sum(LiTy)/len(LiTy)
                preCli = nowCli

        cv2.imshow('MediaPipe Hands', image)
        if cv2.waitKey(5) & 0xFF == 27:
            break
cap.release()
