#! D:\Anaconda3\envs\garbageClassify\python.exe

#语音识别
from aip import AipSpeech

class aipdetect():
    """ 你的 APPID AK SK """
    APP_ID = '33819397'
    API_KEY = '4CPn8BXcCXqRxGbejpG6dFM6'
    SECRET_KEY = 'oaCuE3Ggs8Zq5wL5W5h1YaIEMzrfeKbs'
    def __init__(self) -> None:
        self.client = AipSpeech(self.APP_ID, self.API_KEY, self.SECRET_KEY)

    def detect(self, speech):
        result = self.client.asr(speech, 'pcm', 16000, {
            'dev_pid': 1537,
        })
        return result