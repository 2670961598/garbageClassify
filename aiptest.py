#! D:\Anaconda3\envs\garbageClassify\python.exe

from aipclass.synthesis import aipsynthesis

print("hello world")

#语音合成
synClient = aipsynthesis()

speech = synClient.synthesis("你好")
# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(speech, dict):
    with open('auido.mp3', 'wb') as f:
        f.write(speech)
    print("语音合成成功")

#播放音频
import pygame
import time
time.sleep(0.5)
pygame.mixer.init()
pygame.mixer.music.load('auido.mp3')
pygame.mixer.music.play()


from pydub import AudioSegment

# 读取mp3文件
song = AudioSegment.from_file("auido.mp3", format="mp3")
# 转换为pcm文件
pcmdata = song.export("auido.pcm", format="s16le", parameters=["-ac", "1", "-ar", "16000"])

#语音识别
from aipclass.detect import aipdetect

detClient = aipdetect()

result = detClient.detect(pcmdata)
print(result)



