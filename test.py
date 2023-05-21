import time

import cv2
import numpy as np
from aipclass.synthesis import aipsynthesis
from aip import AipImageClassify
import urllib, sys
import urllib.request, urllib.error
import ssl
import base64
import requests
import pygame
from mutagen.mp3 import MP3

""" 你的 APPID AK SK """
APP_ID = '33824043'
API_KEY = 'fOOX6rD0vTehrGguvAIiqsXs'
SECRET_KEY = 'CaEKn5gYAIwilYPigkMI8uEDVGStNG06'

host = 'https://recover.market.alicloudapi.com'
path = '/recover'
method = 'POST'
appcode = '52be349ce15b418bb1a4dc8fa05a88e5'
querys = 'city=%E4%B8%8A%E6%B5%B7'
bodys = {}

aipClient = aipsynthesis()

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()
	cv2.imshow('frame', frame)
	c = cv2.waitKey(1)
	if c == ord('q'):
		break
	if c == ord('w'):
		try:
			cv2.imwrite("picture.jpg", frame)
			img = open("picture.jpg", "rb").read()
			result = client.advancedGeneral(img)
			print(result)
			print(result['result'][0]['keyword'])
			if '/' in result['result'][0]['keyword']:
				detectResult = result['result'][0]['keyword'].split('/')[0]
			elif '-' in result['result'][0]['keyword']:
				detectResult = result['result'][0]['keyword'].split('-')[0]
			else:
				detectResult = result['result'][0]['keyword']
			respose = requests.get(
				'https://www.mxnzp.com/api/rubbish/type?name=' + detectResult +'&app_id=ndnjuem3tfsjgnmi&app_secret=a2pRVW1rZ3pRMzJHcEprdHdzQ3Fkdz09')
			print(detectResult)
			speechText = ""
			if respose.json()['data']['aim'] != None:
				print(respose.json(), "aim")
				print("hhh")

				speechText += "您的物品可能为" + respose.json()['data']['aim']['goodsName'] + ", 属于" + respose.json()['data']['aim']['goodsType']
				speechResult = aipClient.synthesis(speechText)
			elif respose.json()['data']['recommendList'] != None:
				print(respose.json(), "recommendList")
				for i in respose.json()['data']['recommendList']:
					speechText += "您的物品中可能包含有" + i['goodsName'] + "，属于" + i['goodsType']
				speechResult = aipClient.synthesis(speechText)
			else:
				print(respose.json(), "continue")
				continue
			print(speechText)
			if not isinstance(speechResult, dict):
				with open('audio.mp3', 'wb') as f:
					f.write(speechResult)
			audioLen = MP3('audio.mp3')
			pygame.mixer.init()
			pygame.mixer.music.load(r'audio.mp3')
			pygame.mixer.music.play()
			time.sleep(audioLen.info.length)
			pygame.mixer.quit()
		except Exception as e:
			print(e)


cap.release()  #常规操作
cv2.DestroyAllWindows()


