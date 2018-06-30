#Imports
import speech_recognition as sr
#gtts for tts
from gtts import gTTS
#subprocess for playing audio
import subprocess
#webbrowser to open websites
import webbrowser
#smtplib for sending emails
import smtplib
#re for searching in commands for arguments
import re

def speak(spokenString):
    print(spokenString)
    #create string into mp3 file using gtts
    tts = gTTS(text = spokenString, lang = 'en-uk')
    tts.save('Marvin_Speak.mp3')
    #opening speak file
    proc = subprocess.Popen(['mpg321 Marvin_Speak.mp3'], stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
    (out, err) = proc.communicate()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = )
        audio = r.listen(source)
    data = ""
    try:
      data = r.recognize_google(audio)
      print("You said: " + data)
    except sr.UnknownValueError:
      print("I didnt get that")
    except sr.RequestError as e:
      print("Api or connection is not working.\n The error is {0}".format(e))
    return data

def commands(command):

    if 'open reddit' in command:
        command = command.split(" ")
        subreddit = command[2]
        url = ('https://www.reddit.com/r/' + subreddit)
        webbrowser.open(url, new = 2)
        print('Done!')

    if 'hello' in command:
        speak('Hello')

    if 'standby' in command:
        speak('Going on standby')

    if "where is" in command:
        location = command.split(" ")[2:].join(" ")
        #location = command

        speak("Hold on, I will show you where " + location + " is.")
        url = ("https://www.google.nl/maps/place/" + location + "/&amp;")
        webbrowser.open(url, new = 2)
