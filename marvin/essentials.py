# Imports
from gtts import gTTS # gtts for text to speech
from platform import system # find os type
from subprocess import Popen, PIPE # subprocess for playing audio
from speech_recognition import Recognizer, Microphone, UnknownValueError, RequestError # speech_recognition to turn speech to string

################################
# File for essential functions #
################################

class MarvinEssentials(Exception): pass # class for breaking loops in Marvin_Script.py
def speak(spokenString):
    print(spokenString) # string to speak
    tts = gTTS(text = spokenString, lang = 'en-uk') # create string into mp3 file using gtts
    if system() == 'Windows':
        pass
    else:
        tts.save('Speak.mp3') # save gtts audio as Speak.mp3
        proc = Popen(['mpg321 Speak.mp3'], stdout = PIPE, stderr = PIPE, shell = True) # Popen command with terminal command arguments
        (out, err) = proc.communicate() # opening speak file

def listen():
    r = Recognizer() # less writing
    with Microphone() as source: # using microphone to detect audio
        r.adjust_for_ambient_noise(source, duration = 0.5) #adjust for ambiet sounds for 1 second
        audio = r.listen(source) # listen for audio
    data = '' # set data ad nothing
    try: # in case of errors
        data = r.recognize_google(audio) # recognize with google's speech recognition
        print('You said: ' + data) # write what was heard
    except UnknownValueError: # unknown audio
        print('I didn\'t get that') # when google api didn't understand audio
        data = 'None' # return none
    except RequestError as e: # request error
        print('Api or connection is not working.\n The error is {0}'.format(e)) # when connection or Api offline
        data = 'Broken' # return broken
    return data # return recognized audio as string

def commandInput(type_of_input):
    if type_of_input == 1: # 1 for listening
        input_to_return = listen() # listen
        return input_to_return # return recognized audio as string
    if type_of_input == 0: # 0 for type input
        input_to_return = input('') # get input
        return input_to_return # return text input