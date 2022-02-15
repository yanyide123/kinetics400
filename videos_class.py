# !/usr/bin/env Python3
# _*_ coding: utf-8 _*_
# Author : yanyide
# FILE: videos_class.py
# @Time: 20220215
# Software: PyCharm

"""把videos对应标签的.avi文件转为kinetics400的格式，其中所包含的格式有.csv和.json格式"""
import json

import cv2
import os
import sys
import random
import pandas as pd
from moviepy.editor import *
from time import sleep
from tqdm import tqdm

def get_file_times(filename):
    u"""
    获取视频时长（s:秒）
    """
    clip = VideoFileClip(filename)
    file_time = clip.duration
    # file_time = timeConvert(clip.duration)
    return file_time

# input_path = r"E:\yyy\videos_class_lable\videos"
input_path = ".\\videos"

# print(os.sep)
List = []
lable_list = os.listdir(input_path)
print(lable_list)
for lable in tqdm(lable_list):
    videos_path = os.path.join(input_path, lable)
    # print(videos_path)
    videos_filenames = os.listdir(videos_path)
    # print(len(videos_filenames))
    # print(videos_filenames)
    for videos in videos_filenames:
        videos_avi = os.path.join(videos_path, videos)
        time = get_file_times(videos_avi)
        # print(time)
        start_time = 0.0
        end_time = start_time + time
        # print(end_time)
        List.append([lable, videos_avi, start_time, end_time])
        
# 随机打算选取80%的训练集和20%的测试集
# random.shuffle(List)
# train_List = List[:(int(0.8*len(List))+1)]
# val_List = List[(int(0.8*len(List))+1):]
# df_train = pd.DataFrame(train_List, columns=["label", "video_avi", "start_time", "end_time"])
# df_val = pd.DataFrame(val_List, columns=["label", "video_avi", "start_time", "end_time"])
print(List)
# 将数据保存字典的形式，使用df.sample随机选取80%的训练集和20%的验证集，使用df.insert添加一列
train_json = {}
val_json = {}
df = pd.DataFrame(List, columns=["label", "video_avi", "start_time", "end_time"])
df_train = df.sample(frac=0.8, replace=False, random_state=0)
df_train.insert(4, 'split', "train", allow_duplicates=False)
for train_dict in tqdm(df_train.to_dict(orient="records")):
    print(train_dict)
    train_json.update({
        "---"+train_dict["video_avi"].split("\\")[-1].split(".")[0]:{
            "annotations":{
                "label":train_dict["label"],
                "segment":[train_dict["start_time"], train_dict["end_time"]],
                
            },
            "duration": time,
            "subset":"train",
            "url":train_dict["video_avi"]
        }
    })
df_val = df[~df.index.isin(df_train.index)]
df_val.insert(4, "split", "val", allow_duplicates=False)
for val_dict in tqdm(df_val.to_dict(orient="records")):
    print(val_dict)
    val_json.update({
        "---" + val_dict["video_avi"].split("\\")[-1].split(".")[0]: {
            "annotations": {
                "label": val_dict["label"],
                "segment": [val_dict["start_time"], val_dict["end_time"]],
                
            },
            "duration": time,
            "subset": "val",
            "url": val_dict["video_avi"]
        }
    })
df.to_csv("new.csv", header=True, encoding="utf-8")
df_train.to_csv("new_train.csv", header=True, encoding="utf-8")
df_val.to_csv("new_val.csv", header=True, encoding="utf-8")
