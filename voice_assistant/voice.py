import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import os
import webbrowser

# Initialize the speech engine
engine = pyttsx3.init()

# Set voice properties (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Choose the voice [0] for male and [1] for female

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        listener.adjust_for_ambient_noise(source)
        audio = listener.listen(source)

    try:
        print("Recognizing...")
        command = listener.recognize_google(audio)
        command = command.lower()
        print(f"User said: {command}")
    except sr.UnknownValueError:
        print("Sorry, I did not get that")
        return None
    except sr.RequestError:
        print("Sorry, my speech service is down")
        return None

    return command

def run_voice_assistant():
    command = take_command()

    if command is None:
        return
    
    if 'play' in command:
        song = command.replace('play', '')
        talk(f'Playing {song}')
        pywhatkit.playonyt(song)
    
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f'The current time is {time}')
    
    elif 'search' in command:
        query = command.replace('search', '')
        talk(f'Searching {query} on the web')
        webbrowser.open(f'https://www.google.com/search?q={query}')
    
    elif 'open' in command:
        if 'notepad' in command:
            os.system('notepad.exe')
        elif 'calculator' in command:
            os.system('calc.exe')

    else:
        talk("Sorry, I can't do that yet.")

if __name__ == "__main__":
    talk("How can I assist you?")
    while True:
        run_voice_assistant()
