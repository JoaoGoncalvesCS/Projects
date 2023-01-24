import speech_recognition as sr #Speech Recognition
import playsound #To Play an audio
import random
from gtts import gTTS #Google Text to Speech
import webbrowser #Open Browser
import ssl
import certifi
import time
import os #Remove the audio files
import subprocess
from PIL import Image
import pyautogui
import pyttsx3
import bs4 as bs
import urllib.request

class person:
    name = ""
    def setName(self, name):
        self.name = name

class asis:
    name = ""
    def setName(self, name):
        self.name = name

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

def engine_speak(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()

r=sr.Recognizer() #Initiating the recognizer
#Listen for audio and convert it into text
def record_audio(ask=""):
    with sr.Microphone() as source:
        if ask:
            engine_speak(ask)
        audio = r.listen(source, 5, 5) #Listen for audio via source 
        print("Done Listening")
        voice_data = ""
        try:
            voice_data = r.recognize_google(audio) #Converts audio to text
        except sr.UnknownValueError: #Recognizer does not understand
            engine_speak("Sorry sir, I did not understand it")
        except sr.RequestError:
            engine_speak("Sorry the server is down") #Error the recognizer is not connected
            print(">>", voice_data.lower()) #Print what was said by the user
            return voice_data.lower()

#Get string and make it an audio file to be played
def engine_speak(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang="en") #Text to speech
    r = random.randint(1, 20000000)
    audio_file = "audio" + str(r) + ".mp3"
    tts.save(audio_file) #Save as mp3
    playsound.playsound(audio_file) #Help us to play the audio
    print(asis_obj.name+":", audio_string) #Print what the app said
    os.remove(audio_file)

def respond(voice_data):
    #1 Greeting
    if there_exists(["Hello", "Hi", "Hey"]):
        greetings=["Hey, how can I help you" + person_obj.name, "How can I help you" + person_obj.name, "Hello" + person_obj.name]
        greet = greetings[random.randint(0,len(greetings)-1)]
        engine_speak(greet)

    #2 Name
    if there_exists(["What is your name", "Tell your name"]):
        if person_obj.name:
            engine_speak("I don't know my name, please give me a name by saying a command: Your name should be,,,, what is your name")
        else:
            engine_speak("What's your name sir")

    if there_exists(["My name is"]):
        person_name = voice_data.split("is")[-1].strip()
        engine_speak("Okay sir, I'll remmember that your name is" + person_name())
        person_obj.setName(person_name) #Remmember name in person object
    
    if there_exists(["Your name should be"]):
        asis_name = voice_data.split("be")[-1].strip()
        engine_speak("Okay, I'll remmember that my name is " + asis_name)
        asis_obj.setName(asis_name) #Remmember the name is asis object
    
    #3 Greetings
    if there_exists(["How are you", "How are you doing"]):
        engine_speak("I'm very well, thank you for asking" + person_obj.name)
    
    #4 Time
    if there_exists(["What time is it", "What's the time", "Tell me the time"]):
        time = time.ctime().split(" ")[3].split(":")[0:2]
        if time[0] == "00":
            hours = "12"
        else:
            hours = time[0]
            minutes = time[1]
            time = hours + "hours and" + minutes + "minutes"
            engine_speak(time)
    
    #5 Google search
    if there_exists(["search for"]) and "youtube" not in voice_data:
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?q" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term)

    #6 Youtube search
    if there_exists(["Youtube"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + "on Youtube")

    #7 Get to know a stock price
    if there_exists(["Price of"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?q" + search_term
        webbrowser.get().open(url)
        engine_speak("Here is what I found for" + search_term + "on Google")

    #8 Search for Music
    if there_exists(["Play music"]):
        search_term = voice_data.split("for")[-1]
        url = "https://open.spotify.com/search" + search_term
        engine_speak("You are listening to" + search_term + "enjoy it")
    
    #9 Amazon search
    if there_exists(["Amazon"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.amazon.com/" + search_term
        engine_speak("Here's what I've found for" + search_term + "on Amazon")

    #10 Make a note
    if there_exists(["Make a note"]):
        search_term = voice_data.split("for")[-1]
        url = "http://keep.google.com/#home"
        webbrowser.get().open(url)
        engine_speak("Here you can make notes")

    #11 Open Instagram
    if there_exists(["Open Instagram", "IG"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.instagram.com/"
        webbrowser.get().open(url)
        engine_speak("Opening instagram")
        
    #11 Open Twitter
    if there_exists(["Open Twitter"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.twitter.com/"
        webbrowser.get().open(url)
        engine_speak("Opening Twitter")

    #11 Open Facebok
    if there_exists(["Open Facebook", "Facebook"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.facebook.com/"
        webbrowser.get().open(url)
        engine_speak("Opening facebook")

    #12 Time table
    if there_exists(["Show me my time table"]):
        im = Image.open(r"C:\Users\Joao\Desktop\STScI-01G77PGXFM1NRHYEFRD9VMS26R")
        im.show()
    
    #13 Weather
    if there_exists(["Weather", "Tell me the weather", "What's the conditions outside", "How's the weather today"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?q=weather&oq=weather&aqs=chrome.0.0i512l7j46i512j0i512j46i199i465i512.1162j1j9&sourceid=chrome&ie=UTF-8"
        webbrowser.get().open(url)
        engine_speak("Here is what I've found on Google")

    #14 Open Outlook
    if there_exists(["Open my mail", "Check my mail", "Outlook"]):
        search_term = voice_data.split("for")[-1]
        url = "https://outlook.live.com/mail/0/"
        webbrowser.get().open(url)
        engine_speak("Here's your mail")
    
    #Game (Stone, paper, scizors)
    if there_exists(["Game"]):
        voice_data = record_audio("Choose between rock, paper or scizor")
        moves = ["rock", "paper", "scizor"]
        cmove = random.choice(moves)
        pmove = voice_data
        engine_speak("I choose" + cmove)

        if pmove == cmove:
            engine_speak("It's a draw")
        elif pmove=="rock" and cmove=="paper":
            engine_speak("I won")
        elif pmove=="rock" and cmove=="scizor":
            engine_speak("You won")
        elif pmove=="paper" and cmove=="scizor":
            engine_speak("I won")
        elif pmove=="paper" and cmove=="rock":
            engine_speak("You won")
        elif pmove =="scizor" and cmove=="paper":
            engine_speak("You won")
        elif pmove=="scizor" and cmove=="rock":
            engine_speak("I won")
        
    #Game Toss a coin
    if there_exists(["toss", "flip", "coin"]):
        moves = ["head", "tails"]
        cmove = random.choice(moves)
        engine_speak("The computer chose" + cmove)

    #Calculator
    if there_exists(["plus", "add", "subtract", "minus", "divide", "split", "times", "multiply", "power", "+", "-", "*", "/"]):
        opr = voice_data.split()[1]
        if opr == "+" or opr == "plus" or opr == "add":
            engine_speak(int(voice_data.split()[0]) + int(voice_data.split()[2]))
        elif opr == "-" or opr == "minus" or opr=="subtract":
            engine_speak(int(voice_data.split()[0]) - int(voice_data.split()[2]))
        elif opr == "multiply" or opr == "times":
            engine_speak(int(voice_data.split()[0]) * int(voice_data.split()[2]))
        elif opr == "divide" or opr == "split":
            engine_speak(int(voice_data.split()[0]) / int(voice_data.split()[2]))
        elif opr == "power":
            engine_speak(int(voice_data.split()[0]) ** int(voice_data.split()[2]))
        else:
            engine_speak("Wrong operator")

    #Screenshot
    if there_exists(["Capture", "Screenshot"]):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save("")

time.sleep(1)
asis_obj = asis()
person_obj = person()
asis_obj.name = "Alexa"
engine = pyttsx3.init()

while(1):
    voice_data = record_audio("Recording") #Get the voice input
    print("Done")
    print("Q: ", voice_data)
    respond(voice_data) #Respond 