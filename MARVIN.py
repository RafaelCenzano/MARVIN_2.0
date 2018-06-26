import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()
data = ''

def speak(spokenString):
    print(spokenString)
    tts = gTTS(text = audioString, lang = 'en-uk')
    tts.save('Marvin_Speak.mp3')

def listen():
    with mic as source:
        r.adjust_for_ambient_noise(source, duration = 0.5)
        audio =r.listen(source)
    try:
        data = r.recognize_google(audio)
        print(data)
    except sr.UnknownValueError:
        print('I didn\'t get that')
    except sr.RequestError as e:
        print('The Google Speech Recognition got an error {} ').format (e)
    return data
#print (r.recognize_google(audio))
