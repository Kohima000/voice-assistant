import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import gtts
import os
import time
from playsound import playsound

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def talk(text):
    v = gtts.gTTS(text)
    date_string = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
    file = str(date_string + "song.mp3")
    v.save(file)
    playsound(file)

def speak_now():
    with sr.Microphone() as source:
        print("Speak Now")
        voice=listener.listen(source,10,3)
        try:
            print("Listening")
            command=listener.recognize_google(voice)
            print("You said " + command)
        except sr.UnknownValueError:
            print("oops")
    return command

def run_voiceassistant(command):
    if "hand gesture" not in command:
        talk("speaking " + command)
    if "play" in command:
        song = command.replace("play", "")
        talk("playing for you" + song)
        print("Now playing......")
        pywhatkit.playonyt(song)
    elif "time" in command:
        var_time = datetime.datetime.now().strftime("%I:%M %p")
        print("The current time is " + var_time)
        talk("The current time is " + var_time)
    elif "search" in command:
        res = command.replace("search", "")
        info = wikipedia.summary(res, sentences=2)
        print(info)
        talk(info)
    elif "joke" in command:
        joke=pyjokes.get_joke()
        print(joke)
        talk(joke)
    else:
        if "hand gesture" not in command:
            print("oops didn't get that. Say again!")
            talk("oops didn't get that. Say again!")

while True:
    speech=speak_now()
    if "hand gesture" in speech:
        for file in os.listdir("C:/Users/Kohima/PycharmProjects/virtual assistant/Virtual_Assistant"):
            if file.startswith("gesture.py"):
                exFile=os.path.join("C:/Users/Kohima/PycharmProjects/virtual assistant/Virtual_Assistant", file)
                exec(open(exFile).read())
    if "stop" in speech:
    	break
    else:
    	run_voiceassistant(speech)
    	
