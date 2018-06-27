#Imports
import speech_recognition as sr
from gtts import gTTS
import subprocess

r = sr.Recognizer()
mic = sr.Microphone()
data = ''

def speak(spokenString):
    print(spokenString)
    #create string into mp3 file using gtts
    tts = gTTS(text = spokenString, lang = 'en-uk')
    tts.save('Marvin_Speak.mp3')
    #opening speak file
    proc = subprocess.Popen(['mpg321 Marvin_Speak.mp3'], stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True)
    (out, err) = proc.communicate()

def listen():
    with mic as source:
        #cancel out ambiet noises
        r.adjust_for_ambient_noise(source, duration = 0.5)
        #listen from source
        audio = r.listen(source)
    try:
        #recognize audio
        data = r.recognize_google(audio)
        print(data)
    except sr.UnknownValueError:
        #when google speech recognition doesn't understand what you said
        print('I didn\'t get that')
    except sr.RequestError as e:
        #when theres been an error or failed connections
        print('The Google Speech Recognition got an error {} ').format (e)
    return data

