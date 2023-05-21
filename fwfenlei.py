#! D:\Anaconda3\envs\Pytorch\python.exe
import base64
import cv2
import requests
from urllib import parse
class garbage:
    def __init__(self):
        a=1
    def openCamare(self):
        #打开相机
        cap = cv2.VideoCapture(0)
        #因为某些相机在开机的前几张照片过暗，所以这里使用第十张照片
        for i in range(10):
            #读取相机的照片
            ret ,frame = cap.read()
            #将文件写入文件夹
            cv2.imwrite('./picture.jpg',frame)
        #关闭相机
        cap.release()
    def BaiduAPI(self):
        # client_id 为官网获取的AK， client_secret 为官网获取的SK
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&' \
               'client_id=hZIViGUH1si8lbvRSmuYvMOv&' \
               'client_secret=GVGhfBXZ23CucSLv2d4cHZlVvhRbW1Yq'
        response = requests.get(host)
        if response:
            pass
            #print(response.json())
        res = response.json()
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general"
        # 二进制方式打开图片文件
        f = open('./picture.jpg', 'rb')
        img = base64.b64encode(f.read())
        params = {"image":img}
        #print(params)
        access_token = res['access_token']
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            #得到回复
            #print (response.json())
            self.resp = response.json()
            #print(self.resp['result'][0]['keyword'])

    def classify(self):
        classes = [0,0,0,0]
        for p in self.resp['result']:
            r = ShowapiRequest("http://route.showapi.com/2158-1","865925","b7cc3f68a852444eae55b61a11ccf0f2" )
            r.addBodyPara("word", p['keyword'])
            r.addBodyPara("num", "1")
            r.addBodyPara("page", "1")
            res = r.post().json()
            #print(res)
            if 'newslist' in res['showapi_res_body']:
                print(res['showapi_res_body']['newslist'])# 返回信息
                return
            else:

                pass
                
                #print('这不是垃圾')

files = {}
headers = {}
body = {}
timeouts = {}
resHeader = {}
class ShowapiRequest:
    def __init__(self, url, my_appId, my_appSecret):
        self.url = url
        self.my_appId = my_appId
        self.my_appSecret = my_appSecret
        body["showapi_appid"] = my_appId
        body["showapi_sign"] = my_appSecret
        headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2427.7 Safari/537.36"
    def addFilePara(self, key, value_url):
        files[key] = open(r"%s" % (value_url), 'rb')
        return self

    def addHeadPara(self, key, value):
        headers[key] = value
        return self
    def addBodyPara(self, key, value):
        body[key] = value
        return self
    #设置连接时间和读取时间
    def setTimeout(self, connecttimout, readtimeout):
        timeouts["connecttimout"] = connecttimout
        timeouts["readtimeout"] = readtimeout
        return self
    def get(self):
        get_url = self.url + "?" + parse.urlencode(body)
        if not timeouts:
            res = requests.get(get_url, headers=headers)
        else:
            timeout = (timeouts["connecttimout"], timeouts["readtimeout"])
            res = requests.get(get_url, headers=headers, timeout=timeouts)
        return res

    def post(self):
        if not timeouts:
            res = requests.post(self.url, files=files, data=body, headers=headers)
        else:
            timeout = (timeouts["connecttimout"], timeouts["readtimeout"])
            res = requests.post(self.url, files=files, data=body, headers=headers, timeout=timeout)
        return res



if __name__ == '__main__':
    a = garbage()
    garbage.openCamare(a)
    garbage.BaiduAPI(a)
    garbage.classify(a)
    input()