#Imports
import speech_recognition as sr # speech_recognition to turn speech to string
from gtts import gTTS # gtts for text to speech
import subprocess # subprocess for playing audio
import webbrowser # webbrowser to open websites
import smtplib # smtplib for sending emails

#FUNCTIONS

def speak(spokenString):
    print(spokenString)
    tts = gTTS(text = spokenString, lang = 'en-uk') # create string into mp3 file using gtts
    tts.save('Marvin_Speak.mp3')
    proc = subprocess.Popen(['mpg321 Marvin_Speak.mp3'], stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
    (out, err) = proc.communicate() # opening speak file

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source: # using microphone to detect audio
        r.adjust_for_ambient_noise(source, duration = 1) #adjust for ambiet sounds for 1 second
        audio = r.listen(source) # listen for audio
    data = ''
    try:
        data = r.recognize_google(audio) # recognize with google's speech recognition
        print('You said: ' + data)
    except sr.UnknownValueError:
        print('I didn\'t get that') # when google api didn't understand audio
    except sr.RequestError as e:
        print('Api or connection is not working.\n The error is {0}'.format(e)) # when connection or Api offline
    return data

class MarvinCommands(Exception): pass
def commands(command):

    if 'open reddit' in command:
        subreddit = command.split(" ")[2:] # split for anything after 'open reddit'
        subreddit_joined = (" ").join(subreddit) # joining anything that was split from after 'where is'
        speak('Opening subreddit ' + subreddit_joined) # saying the subreddit page
        url = ('https://www.reddit.com/r/' + subreddit_joined) # url with reddit page
        webbrowser.open(url, new = 2) # open url in browser
        print('Done!')

    if 'hello' in command:
        speak('Hello')

    if 'standby' in command:
        speak('Going on standby')
        raise MarvinCommands # raise exeption so class passes and restarts loop

    if 'where is' in command:
        location = command.split(" ")[2:] # split for anything after 'where is'
        location_joined = (" ").join(location) # joining anything that was split from after 'where is'
        speak('Hold on, I will show you where ' + location_joined + ' is.') # saying the location heard
        url = ('https://www.google.nl/maps/place/' + location_joined + '/&amp;') # url with location
        webbrowser.open(url, new = 2) # open url in browser
        print('Done!')
