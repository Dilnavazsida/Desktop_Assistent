import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
from plyer import notification



engine = pyttsx3.init()

voices = engine.getProperty("voices")

engine.setProperty("rate",150)

def say(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    content = " "
    while content == " ":
        r= sr.Recognizer()
        with sr.Microphone()as sourse:
            print("say something....")
            r.adjust_for_ambient_noise(sourse)  
            audio = r.listen(sourse)

        try:
            content = r.recognize_google(audio,language="en-in")
            print("You said.... ",content)
        except Exception as e:
            print("i couldn't understand the audio please try again",e)
    return content


def main_process():
    while True:
        result = command().lower()
        if "hello" in result:
            say("hello Dil How Can i Help you ")
        elif "open youtube" in result:
            say("opening youtube...")
            webbrowser.open("www.youtube.com")
        
        




main_process()
# say("result")

