import requests
from bs4 import BeautifulSoup
import speech_recognition as sr
import pyttsx3 as p
import playsound 
    


def get_audio():
    r = sr.Recognizer()
    print('initialising the python bot....')
    engine = p.init('sapi5')

    voices = engine.getProperty('voices')
    engine.setProperty('voice' , voices[1].id)
    engine.say("Hey Bhubesh ! welcome this is pythonbot" )
    engine.runAndWait()
    
r  = sr.Recognizer()

with sr.Microphone() as source:
    print("say something")
    audio = r.listen(source)
    print("Done")
        
        
text = r.recognize_google(audio,lang='en')

url =  "https://www.google.co.in/search?q=" + text


response = requests.get(url)
soup = BeautifulSoup(response.text , "lxml")
for item in soup.select(".r a"):
        f_url = item.get('href')
        myurl = f_url.replace(f_url[:7]  ,'')
        myurl = myurl.split('&')
        myurl = myurl[0]
        print(myurl)
        break
        
get_audio()
print('Searching from :\n' + myurl)
f_response = requests.get(myurl)
f_soup = BeautifulSoup(f_response.text , "lxml")

print(f_soup.get_text())

get_audio()
        
        
        
        
        
        
        
        
        
        
        