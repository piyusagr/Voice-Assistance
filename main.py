from multiprocessing.connection import Listener
import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes
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
    elif 'date' in command:
        talk('sorry, i have not free')
    elif 'are you single' in command:
        talk('no, i am not single')
    elif 'joke'  in command:
        joke=pyjokes.get_joke()
        talk(joke)
        print(joke)
    elif 'open youtube' in command:
            talk("Here you go to Youtube\n")
            webbrowser.open("youtube.com")
 
    elif 'open google' in command:
            talk("Here you go to Google\n")
            webbrowser.open("google.com")
 
    elif 'open stackoverflow' in command:
            talk("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")  
    elif 'open github' in command:
           text=command.replace('open github of','')
           talk("here you go to github of"+text)
           webbrowser.open("github.com/"+text)
    elif 'browse'  in command:
           text=command.replace('browse','')
           talk('here you go with'+text)
           webbrowser.open('google.com/'+text)
    else:
        talk('plz say the command again')
        
while True:
    run_alexa()
