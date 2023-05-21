#! D:\Anaconda3\envs\garbageClassify\python.exe

#语音合成
from aip import AipSpeech
class aipsynthesis():
    """ 你的 APPID AK SK """
    APP_ID = '33819397'
    API_KEY = '4CPn8BXcCXqRxGbejpG6dFM6'
    SECRET_KEY = 'oaCuE3Ggs8Zq5wL5W5h1YaIEMzrfeKbs'

    def __init__(self) -> None:

        self.client = AipSpeech(self.APP_ID, self.API_KEY, self.SECRET_KEY)

    def synthesis(self, text):
        # 发送语音
        result = self.client.synthesis(text, 'zh', 1, {
            'vol': 5,
            'per': 0,
            'aue': 3
        })

        return result
    














