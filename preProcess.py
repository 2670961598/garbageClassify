#
# import json
#
# path = "garbage_classification.json"
# data = json.load(open(path, 'r', encoding='utf-8'))
# print(data)
#
# # import os
# import base64
#
# print(base64.b64decode('aHR0cHM6Ly9pbWcxNC4zNjBidXlpbWcuY29tL24wL2pmcy90NjQyMS8zMS8xNzk1Nzc5NS8xODAzNTUvYzU0ZjEyZGEvNTkzN2Q2ZGJOYTAxNTI0MjQuanBn')
# )
# print(base64.b64encode(b'https://pic1.imgdb.cn/item/646a6295e03e90d874f6893f.jpg'))
import requests

respose = requests.get('https://www.mxnzp.com/api/rubbish/type?name=西瓜&app_id=ndnjuem3tfsjgnmi&app_secret=a2pRVW1rZ3pRMzJHcEprdHdzQ3Fkdz09')
print(respose.json())


# dataPath = "Mydata/"
# #搜索所有的文件夹
# dirs = os.listdir(dataPath)
# #遍历所有的文件夹
# for dir in dirs:
#     #读取文件夹下的垃圾图像
#     files = os.listdir(dataPath+dir)
#     print(dir)
#     #遍历所有的图像
#     for file in files:
#         #给每个图像添加标签
#         # print(file)
#         pass

# from ultralytics import YOLO

# # # Load a model
# # model = YOLO('YOLOv8-cls.yaml')  # build a new model from YAML
# # model = YOLO('YOLOv8m-cls.pt')  # load a pretrained model (recommended for training)
# model = YOLO('D:\\Code\\Python\\2023大创结题\\yolov8-cls.yaml').load('D:\\Code\\Python\\2023大创结题\\yolov8m-cls.pt')  # build from YAML and transfer weights

# # Train the model
# model.train(data='mnist160', epochs=100, imgsz=160, workers=0, batch=4, optimizer="Adam")  # train

