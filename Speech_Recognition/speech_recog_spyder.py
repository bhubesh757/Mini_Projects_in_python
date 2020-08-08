import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            pychi_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except  sr.UnknownValueError:
            pychi_speak('sorry , i am uanble recognise the audio')
        except sr.RequestError:
            pychi_speak('Sorry , My speech is Down')
        
        return voice_data

def pychi_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    audio_file = "voice8.mp3"
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file)                              # play the audio file
    pychi_speak(audio_string) # print what app said
    os.system(audio_file) # remove audio file
    
def respond(voice_data):
    if 'what is your name' in voice_data:
         pychi_speak('My name is pypin')
    if 'what time is it' in voice_data:
        pychi_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('what you are interested in ?')
        url = 'https://www.google.com/search?q=' + search
        webbrowser.get().open(url)
        pychi_speak('here is the url what i found for you!! ' + search)
    if 'find location' in voice_data:
        location = record_audio('what is the location ?')
        url = 'https://www.google.nl/maps/place' + location + '/&amp;'
        webbrowser.get().open(url)
        pychi_speak('Here is the location of' + location)
     
pychi_speak('how can I help you')
while 1:
    voice_data = record_audio()
    respond(voice_data)






