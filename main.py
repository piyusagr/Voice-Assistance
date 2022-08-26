from multiprocessing.connection import Listener
import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import webbrowser

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

talk("welcome to voice assistance made by piyush . how can i help you??")
def take_command():
    try:
        with sr.Microphone() as source:
            print('Listenning...')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'alexa' in command:
                command=command.replace('alexa',' ') 
                # t alk(command)      
                print(command)
            
    except:
        pass
    return command

def run_alexa():
    command=take_command()
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%H:%M')
        talk('current time is '+ time)
    
    elif 'tell me about' in command:
        tell=command.replace('tell me about','')
        sourc=wikipedia.summary(tell,1)
        talk(sourc)
        print(sourc)
    
    
run_alexa()