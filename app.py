#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import mediapipe as mp
import numpy as np
import time
import keyboard
import tkinter as tk
from pynput.mouse import Button, Controller
mouse = Controller()
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hotkey = 'F4'


def tk_arg():
    root = tk.Tk()
    root.title("First Setup")
    root.geometry("300x300")
    Val1 = tk.IntVar()
    Val2 = tk.IntVar()
    Val4 = tk.IntVar()
    Val4.set(30)                        # デフォルトマウス感度
    place = ['Normal', 'Over Hand', 'Behind You']
    # Camera #########################################################################
    Static1 = tk.Label(text='Camera').grid(row=1)
    for i in range(3):
        tk.Radiobutton(root,
                       value=i,
                       variable=Val1,
                       text=f'Device{i}'
                       ).grid(row=2, column=i*2)
    St1 = tk.Label(text='     ').grid(row=3)
    # Place #########################################################################
    Static1 = tk.Label(text='How to place').grid(row=4)
    for i in range(3):
        tk.Radiobutton(root,
                       value=i,
                       variable=Val2,
                       text=f'{place[i]}'
                       ).grid(row=5, column=i*2)
    St1 = tk.Label(text='     ').grid(row=6)
    # Sensitivity ###################################################################
    Static4 = tk.Label(text='Sensitivity').grid(row=7)
    s1 = tk.Scale(root, orient='h',
                  from_=1, to=100, variable=Val4
                  ).grid(row=8, column=2)
    St4 = tk.Label(text='     ').grid(row=9)
    # continue
    Button = tk.Button(text="continue", command=root.destroy).grid(
        row=10, column=2)
    # 待機
    root.mainloop()
    # 出力
    cap_device = Val1.get()             # 0,1,2
    mode = Val2.get()                     # 0:youself 1:
    kando = Val4.get()/10               # 1~10
    return cap_device, mode, kando


def draw_circle(image, x, y, roudness, color):
    cv2.circle(image, (int(x), int(y)), roudness, color,
               thickness=5, lineType=cv2.LINE_8, shift=0)


def calculate_distance(l1, l2):
    v = np.array([l1.x, l1.y])-np.array([l2.x, l2.y])
    distance = np.linalg.norm(v)
    return distance


def main(cap_device, mode, kando):
    dis = 0.7                           # くっつける距離の定義
    preX, preY = 0, 0
    nowCli, preCli = 0, 0               # 現在、前回の左クリック状態
    norCli, prrCli = 0, 0               # 現在、前回の右クリック状態
    douCli = 0                          # ダブルクリック状態
    i, k, m = 0, 0, 0
    LiTx = []
    LiTy = []
    nowUgo = 1
    cap_width = 1280
    cap_height = 720
    start, c_start = float('inf'), float('inf')
    c_text = 1
    # Webカメラ入力, 設定
    window_name = 'NonMouse'
    cv2.namedWindow(window_name)
    cap = cv2.VideoCapture(cap_device)
    cfps = int(cap.get(cv2.CAP_PROP_FPS))
    if cfps < 30:
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, cap_width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, cap_height)
        cfps = int(cap.get(cv2.CAP_PROP_FPS))
    # スムージング量（小さい:カーソルが小刻みに動く 大きい:遅延が大）
    ran = int(cfps/10)
    hands = mp_hands.Hands(
        min_detection_confidence=0.8,   # 検出信頼度
        min_tracking_confidence=0.8,    # 追跡信頼度
        max_num_hands=1                 # 最大検出数
    )
    # メインループ ###############################################################################
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
        results = hands.process(image)  # mediapipeの処理
        image.flags.writeable = True    # 画像に手のアノテーションを描画
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        image_height, image_width, _ = image.shape

        if results.multi_hand_landmarks:
            # 手の骨格描画
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # グローバルホットキーが押されているとき ##################################################
            if keyboard.is_pressed(hotkey):
                # print(hand_landmarks.landmark[0])
                # preX, preY, LiTx, LiTyの初期値に現在のマウス位置を代入 1回だけ実行
                if i == 0:
                    preX = hand_landmarks.landmark[8].x
                    preY = hand_landmarks.landmark[8].y
                    for j in range(ran):                # range(ran)の分だけ繰り返す
                        LiTx.append(hand_landmarks.landmark[8].x)
                        LiTy.append(hand_landmarks.landmark[8].y)
                    i = +1

                # 指相対座標の基準距離、以後mediapipeから得られた距離をこの値で割る
                absKij = calculate_distance(
                    hand_landmarks.landmark[0], hand_landmarks.landmark[1])
                # 人差し指の先端と中指の先端間のユークリッド距離
                absUgo = calculate_distance(
                    hand_landmarks.landmark[8], hand_landmarks.landmark[12]) / absKij
                # 人差し指の第２関節と親指の先端間のユークリッド距離
                absCli = calculate_distance(
                    hand_landmarks.landmark[4], hand_landmarks.landmark[6]) / absKij

                # 人差し指の先端をカーソルに対応 && ３つ平均でスムージング
                LiTx.append(hand_landmarks.landmark[8].x)   # 末尾に追加
                LiTy.append(hand_landmarks.landmark[8].y)
                if len(LiTx) > ran:                         # ranを超えたら
                    LiTx.pop(0)                             # 先頭を削除
                    LiTy.pop(0)
                # カメラ座標をマウス移動量に変換
                dx = kando * (sum(LiTx)/ran - preX) * image_width
                dy = kando * (sum(LiTy)/ran - preY) * image_height

                # フラグ #########################################################################
                # click状態
                if absCli < dis:
                    nowCli = 1          # nowCli:左クリック状態(1:click  0:non click)
                    draw_circle(image, hand_landmarks.landmark[8].x * image_width,
                                hand_landmarks.landmark[8].y * image_height, 20, (0, 250, 250))
                elif absCli >= dis:
                    nowCli = 0
                if np.abs(dx) > 3 and np.abs(dy) > 3:
                    k = 0                           # 「動いている」ときk=0
                # 右クリック状態 １秒以上クリック状態&&カーソルを動かさない
                # 「動いていない」ときでクリックされたとき
                if nowCli == 1 and np.abs(dx) < 3 and np.abs(dy) < 3:
                    if k == 0:          # k:クリック状態&&カーソルを動かしてない。113, 140行目でk=0にする
                        start = time.perf_counter()
                        k += 1
                    end = time.perf_counter()
                    if end-start > 1.5:
                        norCli = 1
                        draw_circle(image, hand_landmarks.landmark[8].x * image_width,
                                    hand_landmarks.landmark[8].y * image_height, 20, (0, 0, 250))
                else:
                    norCli = 0
                # print("np.abs(dx)", np.abs(dx))

                # 動かす###########################################################################
                # cursor
                if absUgo >= dis and nowUgo == 1:
                    mouse.move(dx, dy)
                    draw_circle(image, hand_landmarks.landmark[8].x * image_width,
                                hand_landmarks.landmark[8].y * image_height, 8, (250, 0, 0))
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
                    # mouse.release(Button.left)                  # 何故か必要
                    mouse.press(Button.right)
                    mouse.release(Button.right)
                    # print("right click")
                # scroll
                if hand_landmarks.landmark[8].y-hand_landmarks.landmark[5].y > -0.06:
                    mouse.scroll(0, -dy/50)     # スクロール感度:1/6にする
                    draw_circle(image, hand_landmarks.landmark[8].x * image_width,
                                hand_landmarks.landmark[8].y * image_height, 20, (0, 0, 0))
                    nowUgo = 0
                else:
                    nowUgo = 1

                preX = sum(LiTx)/ran
                preY = sum(LiTy)/ran
                preCli = nowCli
                prrCli = norCli
                c_text = 0              # push hotkeyなし
            else:
                c_text = 1              # push hotkeyあり
                #i = 0

        # 表示 #################################################################################
        if c_text == 1:
            cv2.putText(image, f"Push {hotkey}", (20, 450),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
        cv2.putText(image, "cameraFPS:"+str(cfps), (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
        p_e = time.perf_counter()
        fps = str(int(1/(float(p_e)-float(p_s))))
        cv2.putText(image, "FPS:"+fps, (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
        dst = cv2.resize(image, dsize=None, fx=0.4,
                         fy=0.4)         # HDの0.4倍で表示
        cv2.imshow(window_name, dst)
        if (cv2.waitKey(1) & 0xFF == 27) or (cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) == 0):
            break
    cap.release()


if __name__ == "__main__":
    cap_device, mode, kando = tk_arg()
    main(cap_device, mode, kando)
