# Imports
import misc
from wave import open as play # play wav file
from json import load # to open contacts.json to see contacts to be able to send email
from gtts import gTTS # gtts for text to speech
from smtplib import SMTP # smtplib for connection and sending of email
from pyaudio import PyAudio # play wav file
from platform import system # find os type
from subprocess import Popen, PIPE # subprocess for playing audio
from email.mime.text import MIMEText # MIMEText for formatting
from email.mime.multipart import MIMEMultipart # MIMEMultipart changing sender
from speech_recognition import Recognizer, Microphone, UnknownValueError, RequestError # speech_recognition to turn speech to string

################################
# File for essential functions #
################################

class MarvinEssentials(Exception): pass # class for breaking loops in Marvin_Script.py
def speak(spokenString):
    print(spokenString) # string to speak
    tts = gTTS(text = spokenString, lang = 'en-uk') # create string into mp3 file using gtts
    if system() == 'Windows':
        tts.save('Speak.wav') # save gtts as wav
        chunk = 1024 # define stream chunk
        f = play(r"Speak.wav","rb") # open a wav format music
        p = PyAudio() # instantiate PyAudio
        stream = PyAudio().open(format = PyAudio().get_format_from_width(f.getsampwidth()), channels = f.getnchannels(), rate = f.getframerate(), output = True)
        data = f.readframes(chunk) # read data
        while data: # play stream
            stream.write(data)
            data = f.readframes(chunk)
        stream.stop_stream() # stop stream
        stream.close() # close stream
        PyAudio().terminate() # close PyAudio
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
        input_to_return = raw_input('') # get input
        return input_to_return # return text input

def email(recipient, subject, email_message, pass_path, contact_path):
    with open(pass_path, 'r') as email_user_data: # open pass.json to get email password and username
        data = load(email_user_data) # load json
        email_user = data['email_address'] # get email address
        email_pass = data['email_password'] # get email password
    user = misc.checkcontact(contact_path, recipient)
    if user != 'None':
        recipient_email = contact_data['contacts'][user]['email'] # get email address of recipient
        #message area
        marvin_name = ('Marvin <' + email_user + '>')
        msg = MIMEMultipart() # formatting
        msg['From'] = marvin_name
        msg['To'] = recipient_email # input recipient email
        msg['Subject'] = subject # input subject
        msg.attach(MIMEText(email_message,'plain')) # add body
        text = msg.as_string() # format all text

        #sending code
        smtp_server = SMTP('smtp.gmail.com', 587) # connection to 587 port for gmail
        smtp_server.ehlo_or_helo_if_needed()
        smtp_server.starttls() #start connection
        smtp_server.ehlo_or_helo_if_needed()
        smtp_server.login(email_user, email_pass) # login with credentials
        smtp_server.sendmail(email_user, recipient_email, text) # send email
        smtp_server.quit() # quit connection
        print('Email Sent!') # done
    else: # recipient not in contacts
        speak(recipient + ' is not in our contacts use the "add contacts" command to add them') # user not found message

speak('Hello my name is marvin')