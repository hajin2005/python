from gtts import gTTS
from playsound import playsound #mp3 파일을 파이썬으로 재생하기 위한 라이브러리

file_path = 'Mydata.txt'
with open(file_path, 'rt', endcoding='UTF8') as f:
    read_file = f.read()

#text = "나의 살던 고향은 꽃피는 산골"

tts = gTTS(text= read_file, lang='ko')
mp = ("schoolsong.mp3")
tts.save(mp)