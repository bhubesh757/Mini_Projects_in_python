from gtts import gTTS
import time  , os 
import speech_recognition as sr
import webbrowser 
import pyttsx3 as p
import playsound
import requests
from bs4 import BeautifulSoup
    
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'


def speak(text):
    tts = gTTS(text = text , lang = "en")
    filename = "voice1.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


def get_audio():
    r = sr.Recognizer()
    print('initialising the python bot....')
    engine = p.init('sapi5')

    voices = engine.getProperty('voices')
    engine.setProperty('voice' , voices[1].id)
    engine.say("Hey Bhubesh ! welcome this is pythonbot" )
    engine.runAndWait()

    
    with sr.Microphone() as source:
        print("say something")
        audio = r.listen(source)
        print("Done")
        
        try:
            print("Recognizing...")
            query = r.recognize_google(audio , language = 'en-in')
            print(f"user said { query}\n")
        except  sr.UnknownValueError:
            print('sorry , i am uanble recognise the audio')
        except sr.RequestError:
            print('Sorry , My speech is Down')
            query = None
        
    return query

query = get_audio()

if 'open youtube' in query.lower():
    # webbrowser.open("youtube.com")
    url = "youtube.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    speak("opening youtube")
    print("opening youtube")
