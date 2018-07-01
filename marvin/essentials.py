#Imports
import speech_recognition as sr # speech_recognition to turn speech to string
from gtts import gTTS # gtts for text to speech
import subprocess # subprocess for playing audio


################################
# File for essential functions #
################################


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