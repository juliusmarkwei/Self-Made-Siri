import speech_recognition as sr, webbrowser, time, playsound, os, random, pyjokes
from gtts import gTTS
from time import ctime
from pyjokes import *

r = sr.Recognizer()

def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            Amigos_speak(ask)
        print('Say something')
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            Amigos_speak("Sorry something went wrong. Please try again.")
        except sr.RequestError:
            Amigos_speak("Sorry, my speech service is down. Please try again.")
        return voice_data


def Amigos_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if "what is your name" in voice_data:
        Amigos_speak("My name is Amigos")
    if "what time is it" in voice_data:
        Amigos_speak(ctime())
    if "search" in voice_data:
        search = record_audio("what do you want to search for?")
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        time.sleep(1)
        Amigos_speak('Here is what is what I found' + search)
    if "find location" in voice_data:
        location = record_audio("What is the location")
        url = 'https://google.nl/maps/place' + location + "/&amp;"
        webbrowser.get().open(url)
        time.sleep(1)
        Amigos_speak('Here is the location of' + location)
    if "who created you" in voice_data:
        Amigos_speak("Hmmmm,you should have know by now, Mr. Julius Markwei created me")
    if "tell me a joke" in voice_data:
        Amigos_speak(pyjokes.get_jokes())
    if "exit" in voice_data:
        exit()


time.sleep(1)
while 1:
    voice_data = record_audio()
    respond(voice_data)

