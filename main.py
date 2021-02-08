import time
from statics import *
from gtts import gTTS
import random
import playsound
import os
import speech_recognition as sr


def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        text = r.recognize_google(audio)
    return text


def say_message(message):
    voice = gTTS(message, lang="en")
    filename = "_audio_" + str(time.time()) + str(random.randint(0, 100000)) + ".mp3"
    voice.save(filename)
    playsound.playsound(filename)
    print("gTTs: " + message)
    os.remove(filename)


def check_any_set_value_message(set1, message):
    for i in set1:
        if i in message:
            return True
    return False


def do_this_command(message):
    message = message.lower()
    if check_any_set_value_message(greetings, message):
        say_message("Hello!")
    elif check_any_set_value_message(stop_messages, message):
        say_message("Bye!")
        exit()
    else:
        say_message("I don't understand you!")


if __name__ == '__main__':
    while True:
        command = listen_command()
        do_this_command(command)
