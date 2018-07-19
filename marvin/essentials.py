################################
# File for essential functions #
################################

class MarvinEssentials(Exception): pass
def speak(spokenString):
    #Imports
    from gtts import gTTS # gtts for text to speech
    from subprocess import Popen, PIPE # subprocess for playing audio
    #Code
    print(spokenString)
    tts = gTTS(text = spokenString, lang = 'en-uk') # create string into mp3 file using gtts
    tts.save('Marvin_Speak.mp3')
    proc = Popen(['mpg321 Marvin_Speak.mp3'], stdout = PIPE, stderr = PIPE, shell = True)
    (out, err) = proc.communicate() # opening speak file

def listen():
    #Imports
    from speech_recognition import Recognizer, Microphone, UnknownValueError, RequestError # speech_recognition to turn speech to string
    #Code
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

def ADMIN():
    from json import load, dump
    from codecs import encode
    from hashlib import sha512
    from os import system
    while True:
        print('\nOnly use ADMIN acount for administrative tasks')
        print('\n######## ADMIN MENU ########\n\n1. Create New User\n2. Update Marvin\n3. Leave ADMIN Menu')
        ADMIN_input = raw_input('>')
        if ADMIN_input == '1' or 'user' in ADMIN_input.lower():
            print('You will choose a username and password for the new user\nType a User')
            new_user = raw_input('>')
            with open('marvin/json/pass.json', 'r') as login_data:
                new_user_data = load(login_data)
            search_login = new_user_data['logins']
            if new_user in search_login:
                print('This user exists already')
            else:
                print('\nType a password for the new user')
                new_user_pass = raw_input('>')
                new_user_pass_encrypted = sha512(new_user_pass + new_user).hexdigest()
                print('Creating User')
                with open('marvin/json/pass.json', 'w') as outfile:
                    new_user_data['logins'][new_user] = {"pass":new_user_pass_encrypted}
                    dump(new_user_data, outfile)
                print('New user created')
        elif ADMIN_input == '2' or 'update' in ADMIN_input.lower():
            ('Checking for Update')
            system('git pull')
        elif ADMIN_input == '3' or 'exit' in ADMIN_inputor or 'leave' in ADMIN_input or 'quit' in ADMIN_input:
            ('Exiting ADMIN MENU')
            break

def listofcontacts(contact_list):
    import time
    time.sleep(0.7)
    for c in contact_list:
        c_letters = list(c)
        c_letter_first = c_letters[0]
        c_letters_rest = c_letters[1:]
        c_letters_rest_joined = ("").join(c_letters_rest)
        c_letter_first_upper = str(c_letter_first.upper())
        print(c_letter_first_upper + c_letters_rest_joined)

def contactList():
    from threading import Thread
    from json import load
    with open('marvin/json/contacts.json', 'r') as contact_data_list:
        list_contact_data = load(contact_data_list)
        contact_list = list_contact_data['contacts']
    if not contact_list['contacts']:
        print('No contacts use the add contacts command to add some')
        raise MarvinEssentials
    elif not contact_list:
        print('Fatal Error\nMissing data make sure that you ran setup.py before running this script')
        raise MarvinEssentials
    else:
        thread_list_contact = Thread(target = listofcontacts, args=contact_list)
        thread_list_contact.start()
        speak('Opening contact list for you now')

def openCalculator():
    from os import system
    system('python2.7 marvin/calculator.py')

def email(recipient, subject, email_message):
    #import
    from smtplib import SMTP # smtplib for connection and sending of email
    from email.mime.text import MIMEText # MIMEText for formatting
    from email.mime.multipart import MIMEMultipart # MIMEMultipart changing sender
    from json import load # to open contacts.json to see contacts to be able to send email

    recipient_lowered = recipient.lower()
    with open('marvin/json/pass.json', 'r') as email_user_data: # open pass.json to get email password and username
        data = load(email_user_data) # load json
        email_user = data['email_address'] # get email address
        email_pass = data['email_password'] # get email password

    with open('marvin/json/contacts.json', 'r') as contacts_open: # get contact data
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
        server = SMTP('smtp.gmail.com', 587) # connection to 587 port for gmail
        server.starttls() #start connection
        server.login(email_user, email_pass) # login with credentials
        server.sendmail(email_user, recipient_email, text) # send email
        server.quit() # quit connection
        print('Email Sent!') # done
    else: # recipient not in contacts
        speak(recipient + ' is not in our contacts use the "add contacts" command to add them')