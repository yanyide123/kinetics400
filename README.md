# kinetics400
把videos对应标签的.avi文件转为kinetics400的格式，其中所包含的格式有.csv和.json格式
### 实现功能

把videos对应标签的.avi文件转为kinetics400的格式，其中所包含的格式有.csv和.json格式

### 运行环境

python3.6.13

### 数据形式

原始数据形式：

```
|-- data
    |-- label
        |--*.avi
        ...
```

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

