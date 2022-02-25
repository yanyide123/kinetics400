"""
将数据生成Video_swin_trainsformer可以训练的.txt
"""
# import cv2
import os
import sys
# import mmcv
import random
from tqdm import tqdm
import pandas as pd
from moviepy.editor import *

def get_file_times(filename):
    u"""
    获取视频时长（s:秒）
    """
    clip = VideoFileClip(filename)
    file_time = clip.duration
    # file_time = timeConvert(clip.duration)
    return file_time


input_path = r"E:\videos_data_kinetics\videos"
output_path = r"E:\videos_data_kinetics\kinetics400_model_train\data"
if not os.path.exists(output_path):
    os.makedirs(output_path)
List = []
new_List = []
lable_list = os.listdir(input_path)
class_mapping = {lable: i for i, lable in enumerate(lable_list)}
# print(lable_list)
for lable in tqdm(lable_list):
    videos_path = os.path.join(input_path, lable)
    # print(videos_path)
    videos_filenames = os.listdir(videos_path)
    for videos in tqdm(videos_filenames[:10]):
        videos_avi = os.path.join(videos_path, videos)
        # print(videos_avi)
        time = get_file_times(videos_avi)
        start_time = 0.0
        end_time = start_time + time
        List.append([lable, videos_avi, start_time, end_time])
        new_List.append([lable + "/" + videos + " " + str(class_mapping[lable])])


# print(new_List)
df = pd.DataFrame(new_List)
df.to_csv(output_path + "/new_list.txt", index=False, header=False, encoding='utf-8')
# 根据自己的要求去更改训练集和测试集的比例frac(对应自己设置参数)
df_train = df.sample(frac=0.8, replace=False, random_state=0)
df_val = df[~df.index.isin(df_train.index)]
df_train.to_csv(output_path + "/new_list_train.txt", header=False, encoding="utf-8", index=False)
df_val.to_csv(output_path + "/new_list_val.txt", header=False, encoding="utf-8", index=False)


# 以下注释方法也可以按比例拆分训练集和测试集
# random.shuffle(List)
# train_List = List[:(int(0.8*len(List))+1)]
# val_List = List[(int(0.8*len(List))+1):]
# df_train = pd.DataFrame(train_List, columns=["label", "video_avi", "start_time", "end_time"])
# df_val = pd.DataFrame(val_List, columns=["label", "video_avi", "start_time", "end_time"])
# df_train.insert(4, 'split', "train", allow_duplicates=False)
# df_val.insert(4, "split", "val", allow_duplicates=False)
# df.to_csv("new.csv", header=True, encoding="utf-8")
# df_train.to_csv("new_list_train.txt", header=False, encoding="utf-8", index=False)
# df_val.to_csv("new_list_val.txt", header=False, encoding="utf-8", index=False)

