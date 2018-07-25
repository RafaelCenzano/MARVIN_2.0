# Imports
from smtplib import SMTP # smtplib for connection and sending of email
from email.mime.text import MIMEText # MIMEText for formatting
from email.mime.multipart import MIMEMultipart # MIMEMultipart changing sender
from json import load # to open contacts.json to see contacts to be able to send email
from gtts import gTTS # gtts for text to speech
from subprocess import Popen, PIPE # subprocess for playing audio
from speech_recognition import Recognizer, Microphone, UnknownValueError, RequestError # speech_recognition to turn speech to string

################################
# File for essential functions #
################################

class MarvinEssentials(Exception): pass
def speak(spokenString):
    print(spokenString)
    tts = gTTS(text = spokenString, lang = 'en-uk') # create string into mp3 file using gtts
    tts.save('Marvin_Speak.mp3')
    proc = Popen(['mpg321 Marvin_Speak.mp3'], stdout = PIPE, stderr = PIPE, shell = True)
    (out, err) = proc.communicate() # opening speak file

def listen():
    r = Recognizer()
    with Microphone() as source: # using microphone to detect audio
        r.adjust_for_ambient_noise(source, duration = 0.5) #adjust for ambiet sounds for 1 second
        audio = r.listen(source) # listen for audio
    data = ''
    try:
        data = r.recognize_google(audio) # recognize with google's speech recognition
        print('You said: ' + data)
    except UnknownValueError:
        print('I didn\'t get that') # when google api didn't understand audio
        data = 'None'
    except RequestError as e:
        print('Api or connection is not working.\n The error is {0}'.format(e)) # when connection or Api offline
        data = 'Broken'
    return data

def commandInput(type_of_input):
    if type_of_input == 1:
        input_to_return = listen()
        return input_to_return
    if type_of_input == 0:
        input_to_return = raw_input('')
        return input_to_return
    else:
        print('Fatal Error create Issue on Github')

def email(recipient, subject, email_message, pass_path, contact_path):
    recipient_lowered = recipient.lower()
    with open(pass_path, 'r') as email_user_data: # open pass.json to get email password and username
        data = load(email_user_data) # load json
        email_user = data['email_address'] # get email address
        email_pass = data['email_password'] # get email password

    with open(contact_path, 'r') as contacts_open: # get contact data
        contact_data = load(contacts_open) # load contacts data
    if recipient_lowered in contact_data['contacts']: # check if recipient in contacts
        recipient_email = contact_data['contacts'][recipient_lowered]['email'] # get email address of recipient
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
        speak(recipient + ' is not in our contacts use the "add contacts" command to add them')