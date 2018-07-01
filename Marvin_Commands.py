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
    #using microphone to detect audio
    with sr.Microphone() as source:
        #adjust for ambiet sounds
        r.adjust_for_ambient_noise(source, duration = 1)
        #listen
        audio = r.listen(source)
    data = ""
    try:
      #recognize with google's speech recognition
      data = r.recognize_google(audio)
      print("You said: " + data)
    except sr.UnknownValueError:
      #when google api didn't understand audio
      print("I didn\'t get that")
    except sr.RequestError as e:
      #when connection or Api offline
      print("Api or connection is not working.\n The error is {0}".format(e))
    return data

class MarvinCommands(Exception): pass
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
        raise MarvinCommands

    if "where is" in command:
        location = command.split(" ")[2:].join(" ")
        speak("Hold on, I will show you where " + location + " is.")
        url = ("https://www.google.nl/maps/place/" + location + "/&amp;")
        webbrowser.open(url, new = 2)
