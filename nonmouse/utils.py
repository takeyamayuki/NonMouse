#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import numpy as np


def draw_circle(image, x, y, roudness, color):
    """draw circle"""
    cv2.circle(image, (int(x), int(y)), roudness, color,
               thickness=5, lineType=cv2.LINE_8, shift=0)


def calculate_distance(lankdmark1, landmark2):
    """
    Calculate Euclidean distance

    Parameters
    ----------
    landmark1 : list
    landmark2 : list

    Returns
    -------
    distance : float
    """
    v = np.array([lankdmark1[0], lankdmark1[1]]) - \
        np.array([landmark2[0], landmark2[1]])
    distance = np.linalg.norm(v)
    return distance


def calculate_moving_average(landmark, ran, LiT):   # (座標、いくつ分の平均か、移動平均を格納するリスト)
    """
    Calculate moving averages

    Parameters
    ----------
    landmark : list
        landmark
    ran : int
        range
    LiT : list
        list in time

    Returns
    -------
    moving average : float
    """

    while len(LiT) < ran:               # ran個分のデータをLiTに追加（最初だけ）
        LiT.append(landmark)
    LiT.append(landmark)                # LiTの更新（最後に追加）
    if len(LiT) > ran:                  # LiTの更新（最初を削除）
        LiT.pop(0)
    return sum(LiT)/ran
