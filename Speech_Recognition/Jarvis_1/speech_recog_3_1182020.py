from gtts import gTTS
import time  , os 
import speech_recognition as sr
import webbrowser 
import pyttsx3 as p
import playsound
import requests
from bs4 import BeautifulSoup
import datetime
import smtplib

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

Master = "Bhubesh"
def speak(text):
    tts = gTTS(text = text , lang = "en")
    filename = "voice8.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
    
def sndmail(tp , content):
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.ehlo()
    server.starttls()
    server.login('' , '')
    server.sendmail("sarebhyu@gmail.com" , to , content)
    server.close()


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


elif 'open google' in query.lower():
    url = "google.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    speak("opening google") 
    
elif "open reddit" in query.lower():
    url = "reddit.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    speak("opening reddit") 
    print("openning rddit" )
    
elif 'find location' in query.lower():
        location = get_audio('what is the location ?')
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        url = 'https://www.google.nl/maps/place' + location + '/&amp;'
        webbrowser.get().open(url)
        speak('Here is the location of' + location)
    
elif " play me a  music" in query.lower():
    songs_dir = "C:\\Users\\BHUBESH\\Desktop\\songs\\Despacito ft. Daddy Yankee-(MrPaji.com)"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir , songs[0]))
    
elif "whats the time" in query.lower():
    strTime = datetime.datetime.now().strftime("%H : %M :%S")
    speak(f"{Master} the time is {strTime}")

elif "open inkedin" in query.lower():
    url = "linkedin.com"
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    speak("opening linked in ") 
    print("opening linked in" )
    

    

    
    
    

    
    
    
  
    
    