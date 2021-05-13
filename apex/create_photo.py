#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import numpy as np
import os

import math
import glob


# 1秒ごとにTrueを出力
def sec_count(cap_sec, prop_frame, get_sec = 1/20):
    if round(cap_sec) != 0:
        #print(" cap_sex & max_sec is same not")
        if prop_frame%2 == 0:
            print("prop_frame is ", prop_frame)
            print("True ")
            return True
        else:
            return False
    else:
        return False

# ------------------------------------------------main-------------------------------------------------------------

def video_to_img(video_name, save_file, create_list=True):
    """
    cv2.VideoCaptureを使用するには, ffmpegをインストール
    pip install ffmpeg-python

    Example:
    video_name = ./20.10.12_videos/125_0005.MP4
    save_file = ./21.10.12_videos/
    """

    cap = cv2.VideoCapture(video_name)
    print("video ", cap.isOpened())
    ret, frame = cap.read()
    max_frame = cv2.CAP_PROP_FRAME_COUNT
    index_of_photo = 1

    if create_list == True:
        print("create list is true")
        img_list = []

    while(ret == True):
        print("FPS is ", cv2.CAP_PROP_FPS)
        ret, frame = cap.read()
        bool_of_fivesec = sec_count(cap.get(cv2.CAP_PROP_POS_MSEC)/1000, cap.get(cv2.CAP_PROP_POS_FRAMES))
        if bool_of_fivesec == True:
            img = frame.astype(np.uint8)
            if create_list == True:
                img_list.append(img)
                print("list have ", len(img_list))
    
                cv2.imwrite(save_file + '/photo_{}.jpg'.format(str(index_of_photo).zfill(4)), img)
                print(save_file, '/photo_{}.jpg was saved.'.format(str(index_of_photo).zfill(4)))
            index_of_photo += 1

    if create_list == True:
        print("img list is ", np.shape(img_list))
    print('Finished!!')




print(os.getcwd())
print(cv2.getBuildInformation())
video_name = "./data/out.mp4"
save_file = "./data/photo/"
video_to_img(video_name, save_file, create_list=True)
