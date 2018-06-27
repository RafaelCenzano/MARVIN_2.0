#Imports
import speech_recognition as sr
import Marvin_commands as marvin

r = sr.Recognizer()
mic = sr.Microphone()
data = ''

def listen():
    with mic as source:
        r.pause_threshold = 1
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

marvin.speak('Hello my name is Marvin')

command = listen()

marvin.commands(command)