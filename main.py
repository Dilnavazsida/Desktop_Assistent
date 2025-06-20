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
        
        elif "naat sharif" in result.lower():
                    say("playing Naat...")
                    webbrowser.open("https://www.youtube.com/watch?v=i8YyekWrbhU&ab_channel=SafaIslamic")
        elif "nusrat" in result.lower() or "qawwali" in result.lower():
                    say("playing nusrat fateh khan qawali...")
                    webbrowser.open(" https://www.youtube.com/watch?v=k9plOYAmpBU&ab_channel=Atiq%27sCreations")
        elif "current time" in result:
                    now_time = datetime.datetime.now().strftime("%H:%M")
                    say("Current time is "+str(now_time)) 

         if "open" in result:
            query = result.replace("open", "").strip()
            say(f"Opening {query}, sir.")
            pyautogui.press("win")  # Use 'win' for Windows
            time.sleep(1)
            # Wait 1 second so the Start menu loads fully.
            pyautogui.typewrite(query)
            time.sleep(1)
            # Wait for the app to show up in the Start menu.
            pyautogui.press("enter")




main_process()
# say("result")

