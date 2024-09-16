import speech_recognition as sr
import pyttsx3
import datetime
import requests
import webbrowser
import os

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        sound = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(sound)
            print("You said: " + text)
            return text.lower()
        
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return None
        
        except sr.RequestError:
            speak("Sorry, I could not connect to the service")
            return None
        
        return text

def perform_task(command):
    task = listen()

    if task is None:
        return

    if 'time' in command:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {now}")

    elif 'search' in command:
        query = command.replace('search', '')
        speak(f"Searching {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif 'open' in command:
        if 'notepad' in command:
            os.system("notepad.exe")
        elif 'calculator' in command:
            os.system('calc.exe')

    else:
        speak("Sorry, I can not do that yet.")

if __name__ == "__main__":
    speak("How can I assit you?")
    while True:
        perform_task()    