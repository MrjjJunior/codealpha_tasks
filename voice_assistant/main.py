import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import datetime

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set voice properties
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Change to voices[1].id for a female voice
engine.setProperty('rate', 150)  # Speed of speech

def speak(text):
    """This function converts text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """This function listens to the microphone and converts speech to text."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-US')
            print(f"You said: {query}")
            return query.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't get that. Please try again.")
            return ""
        except sr.RequestError:
            speak("Sorry, there is an issue with the speech service.")
            return ""

def greet():
    """This function greets the user based on the time of the day."""
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

def process_command(command):
    """This function processes the voice commands."""
    if 'wikipedia' in command:
        speak('Searching Wikipedia...')
        command = command.replace('wikipedia', '')
        try:
            results = wikipedia.summary(command, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        except wikipedia.exceptions.DisambiguationError as e:
            speak("There are multiple results for this query.")
        except wikipedia.exceptions.PageError:
            speak("No matching Wikipedia page found.")
    
    elif 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif 'open google' in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    
    elif 'what time is it' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"It is {time}")

    elif 'goodbye' in command or 'exit' in command:
        speak("Goodbye!")
        exit()

    else:
        speak("I am sorry, I don't know how to help with that.")

# Main function to run the assistant
def run_assistant():
    greet()
    while True:
        command = listen()
        if command:
            process_command(command)

# Run the assistant
if __name__ == "__main__":
    run_assistant()

