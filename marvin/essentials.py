# Imports
from os import path, remove # import os
from gtts import gTTS # gtts for text to speech
from pyttsx3 import init # pyttsx3 for male voice
from platform import system # find os type
from playsound import playsound
from subprocess import Popen, PIPE # subprocess for playing audio
from speech_recognition import Recognizer, Microphone, UnknownValueError, RequestError # speech_recognition to turn speech to string


################################
# File for essential functions #
################################


def speak(spokenString, voice):
    print(spokenString) # string to speak
    if voice == 'female':
        if path.isfile("Speak.mp3"):
            remove("Speak.mp3")
        tts = gTTS(text = spokenString, lang = 'en-uk') # create string into mp3 file using gtts
        tts.save('Speak.mp3') # save gtts audio as Speak.mp3
        if system() == 'Windows':
            playsound('Speak.mp3')
        else:
            proc = Popen(['mpg321 Speak.mp3'], stdout = PIPE, stderr = PIPE, shell = True) # Popen command with terminal command arguments
            (out, err) = proc.communicate() # opening speak file
    else:
        engine = init()
        engine.say(spokenString)
        engine.runAndWait()

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

def splitJoin(command, how_many):
    split_command = command.split(" ")[how_many:] # split for anything after any unnecessary words
    joined_command = (" ").join(split_command) # joining anything that was split from after any unnecessary words
    return joined_command # return rejoined command