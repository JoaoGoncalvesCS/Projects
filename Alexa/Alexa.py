import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


def talk(text):
    engine.say(text)
    engine.say(text)
    engine.runAndWait()


def get_command():
    try:
        with sr.Microphone() as source:
            print("Listening")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "Alexa" in command:
                command = command.replace("Alexa", "")
                print(command)
    except:
       pass
    return command

while True:
    def run():
        command = get_command()
        if "play" in command:
            song = command.replace("play", "")
            talk("Playing" + song)
            pywhatkit.playonyt(song)
        elif "time" in command:
            time = datetime.datetime.now().strftime("%I:$M:%S %p")
            print(time)
            talk("Current time is" + time)
        elif "search" in command:
            person = command.replace("search", "")
            information = wikipedia.summary(person)
            print(information)
            talk(information)
        elif "joke" in command:
            talk(pyjokes.get_joke())
            print(pyjokes.get_joke())
        else:
            talk("Please repeat it")

run()