#virtualenv jarvis
#pip install pyttsx3 --> it used to convert text to speech
#pip install SpeechRecognition

import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speek(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
def tellTime():
    time = datetime.datetime.now().strftime("%I:%M:%S")
    speek("the current time is")
    speek(time)
    
    
def tell():
    speek("Hello Sir")
    speek("Let's Change The World")

    
    


tell()