import speech_recognition as sr
import pyttsx3 as p

r = sr.Recognizer()
print('initialising the python bot....')
engine = p.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[1].id)
engine.say("Hey Bhubesh ! welcome this is pythonbot" )
engine.runAndWait()

with sr.Microphone() as source:
    text = r.listen(source)
    
    try:
        recognised_text = r.recognize_google(text)
        print(recognised_text)
    except sr.UnknownValueError:
        print('sorry i am unable to recognise the voice')
    except sr.RequestError:
        print("Sorry , My speech is Down")
    text1 = r.listen(source)
    
    try:
        recognised_text1 = r.recognize_google(text1)
        print(recognised_text1)
    except sr.UnknownValueError:
        print('sorry i am unable to recognise the voice')
    except sr.RequestError:
        print("Sorry , My speech is Down")
        
    engine.say("what you would you like to do")
    engine.runAndWait()
    
    

        
# text to speech
























