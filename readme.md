# Videos data kinetics new



## Updates

**02/24/2022** Initial commits

## Introduction

把训练数据data对应label的.avi文件转为kinetics400官方提供原始数据的格式和数据训练的格式。

## Results

kinetics400 official raw format完成的格式，具体见kinetics400 official raw format的READM.md

kinetics400的json格式:

```
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
```

kinetics400的csv格式:

```
标签    label            id           time_start   time_end     split
数据   testifying   --3ouPhoy2A        20          30         train
```



kinetics400 model data type完成的格式，具体见kinetics400 model data type的[READM.md](kinetics400_model_data_type/README.md)]

```
|-- data
    |-- videos
    	|--lable1
    		|--*.avi
    	|--lable2
    		|--*.avi
    
	|-- videos_list
        |-- train.txt
        |-- val.txt
        ...
```

**Notes**:

数据train.txt存储的是相对路径，存储为label/*.avi   lable.

数据val.txt和train.txt一样

## Usage

### Installation

#### Requirements

- Python 3.6+
- Linux (Windows is officially supported)

### Data Preparation

根据训练模型的需要准备数据集，原始数据集的格式：

```
|-- data
    |-- videos
    	|--lable1
    		|--*.avi
    	|--lable2
    		|--*.avi
    	...
```

### Implement

运行 videos_class.py

运行 kinetics_videos.py

**Notes**: 文件路径根据需要更改input、output,进入对应文件夹去执行文件