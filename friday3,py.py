from email.mime import audio
from fileinput import close
from http import server
from re import A
from time import sleep
from unittest import result
import pyttsx3
from bs4 import BeautifulSoup
import requests
import subprocess
import random
import smtplib
import webbrowser
import pywhatkit
import pywhatkit as kit
import datetime
import wikipedia
import os
import speech_recognition as lg

engine = pyttsx3.init('sapi5')
voices  = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
 # getter method(gets the current value
    # of engine property)
     # This loop is infinite as it will take
    # our queries continuously until and unless
    # we do not say bye to exit or terminate
def speak(audio):
   engine.say(audio)
   engine.runAndWait()
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning Sidh Sir. I am Your PC Assistant Friday How may i assist you ")

    elif hour >=12 and hour<18:
        speak("Good Afternoon Sir,!I am Your PC Assistant Friday How may i assist you  ")

    else:
        speak("Good Evening Sir!, I am Your PC Assistant Friday How may i assist you")


def takeCommand():
   a = lg.Recognizer()
   with lg.Microphone() as source:
    print("Listening...")
    a.pause_threshold = 1
    a.dynamic_energy_threshold = 1
    audio = a.listen(source)

    try:
        print("Recongizing...")
        query = a.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
    #    print(e)
       speak('Sorry Can you say that again sir')
       print("Say that Again Sir ")
       return "None"
    return query

def TaskExe():
  speak('Hello Sir, I am Your PC Assistant Friday How can i help you')

if __name__ == "__main__":
 wish()
 while True:
  query = takeCommand().lower()

# Send Email Function
  

 # Logic for Jarvis
  if 'wikipedia' in query:
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    speak(results)
  
  elif 'open youtube' in query:
    speak('Opening YouTube')
    webbrowser.open("youtube.com")

  elif 'open google' in query:
    speak('Opening Google')
    webbrowser.open("google.com")

  elif 'open chrome' in query:
    speak('Opening Google Chrome')
    webbrowser.open("chrome.exe")

  elif 'open gmail' in query:
    speak('Opening Gmail')
    webbrowser.open("gmail.com")
    
  elif 'what is the time'  in query:
    strTime = datetime.datetime.now().strftime("%h:%M:%S")
    speak(f"Sir the Current time is {strTime}")


  elif 'open vs code' in query:
   VsCodePath = "C:\\Users\\ASHUTOSH\\AppData\\Roaming\\Microsoft\\Windows\Start Menu\\Programs\\Visual Studio Code"
   speak("Opening Visual Studio Code")
   os.startfile(VsCodePath)

  elif 'open spotify' in query:
   Spotify = "spotify.exe"
   speak("Opening Spotify Music")
   os.startfile(Spotify)
   

  elif ' play music' in query:
            music_dir = 'G:\\sweedy\\songs'
            songs = os.listdir(music_dir)
            print(songs) 
            speak('enjoy your music sir')   
            os.startfile(os.path.join(music_dir, songs[0]))
  
  elif ' close music' in query:
     speak('ok sir closing music')
     os.close(songs)        

  
  


  elif 'Good job friday' in query:
     speak("Thank you Sir, I Love You")
     

  elif 'you can sleep now friday' in query:
     speak("Ok Sir, You can Wake me up later")
     break

  elif 'how are you' in query:
     speak("I'm Fine, How are you?")

  elif 'who created you' in query:
     speak("I was created by Sir Sidh Prakash")

  elif 'are you better than google assistant' in query:
     speak(" i am just a normal artificail intellignece and google is suprerior")

  elif 'are you better than siri' in query:
     speak("If you can make me more powerful wooh!")

  elif 'are you better than alexa' in query:
     speak("I Love My Dear Alexa")

  elif 'who are you' in query:
     speak("I am Friday, A voice assistant progarm created by  sir sidh prakash")
     
  elif 'i am fine' in query:
     speak("great! ")

  elif 'i am fine' in query:
     speak("great! ")

  elif 'will you marry me' in query:
     speak("no")

  elif 'you are bad' in query:
     speak("sad to hear but, i will try my best to improve and not upset you sorry for that")
   

  elif 'sing a song' in query:
    speak("Yes I can sing. I like to help you, even if it's strange. So I sing.")
  
  elif "tell me a joke" in query:
    speak("Why shouldn't you write with a broken pencil? Because it's pointless")
  elif "who is my school computer teacher" in query:
     speak("ooh! that fat ass , he is none other than naveen anthony,  a total bulshit ,motherfucker,white nigga,he is tharki, and he doesnt know importantance of logics and concepts")
     print("ooh! that fat ass , he is none other than naveen anthony,  a total bulshit ,motherfucker,white nigga,he is tharki, and he doesnt know importantance of logics and concepts")
  
  
  
  elif "tell me more joke" in query:
    speak("what will we called mr bean if he slepp,soya been") 
  elif "shut up friday" in query:
     speak("saale tujhe bolna to bahe ga ,jo ukarna hai ukarna ukhar") 
   
  elif "lame" in query:
    speak("Ok I Will try My Best")
   
  elif "lets distribute sweats to poor " in query:
     speak("give me money sir")
   

# Open CMD
  elif 'open cmd' in query:
    CMD = "cmd.exe"
    speak("Opening Command Prompt")
    os.startfile(CMD)

# Open Pycharm

# Close CMD
  elif 'close cmd' in query:
     CMD = "cmd.exe"
     speak("Closing Command Prompt")
     os.close(CMD)

  elif 'open notepad' in query:
     Notepad = "notepad.exe"
     speak("Opening Notepad")
     os.startfile(Notepad)

# Close Friday 
  elif 'sleep friday' in query:
     CMD = "cmd.exe"
     speak("Putting To Sleep, you can wake me up")
     os.close(CMD)
     
     
  elif ' open my favourite playlist ' in query:
     speak("Sure Sir Enjoy Your Music ")
     webbrowser.open("https://open.spotify.com/playlist/6nwSjsPNsvFh4iVm2Z4uzb")
        

# Send Mail  
 
        

# temperature
 
    