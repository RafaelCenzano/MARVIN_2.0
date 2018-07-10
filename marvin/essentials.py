################################
# File for essential functions #
################################


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
    except RequestError as e:
        print('Api or connection is not working.\n The error is {0}'.format(e)) # when connection or Api offline
    return data

class MarvinEmail(Exception): pass
def email(recipient, subject, email_message):
    #import
    from smtplib import SMTP
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from json import load

    with open('../pass.json', 'r') as email_user_data:
        data = load(email_user_data)
        email_user = data['email_address']
        email_pass = data['email_password']

    with open('marvin/json/contacts.json', 'r') as contacts_open:
        contact_data = load(contacts_open)
    if recipient in contact_data['contacts']:
        recipient_email = contact_data['contacts'][recipient]['email']
    else:
        speak(recipient + ' is not in our contacts use the "add contacts" command to add them')
        raise MarvinEmail

    #message area
    msg = MIMEMultipart()
    msg['From'] = 'Marvin'
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(email_message,'plain'))
    text = msg.as_string()

    #sending code
    server = SMTP('smtp.gmail.com', 587) # connection to 587 port for gmail
    server.starttls() #start connection
    server.login(email_user, email_pass) # login with credentials
    server.sendmail(email_user, recipient_email, text) # send email
    server.quit() # quit connection
    print('Done!') # done