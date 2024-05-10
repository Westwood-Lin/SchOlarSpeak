import speech_recognition as sr
import pyaudio
import pocketsphinx
import time
import pyttsx3


def audio2text():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("listening")
        audio = r.listen(source)

    c = r.recognize_sphinx(audio, language='en-US')
    print(c)
    return c


def text2audio(text):
    pyttsx3.speak(text=text)


if __name__ == '__main__':
    text = audio2text()
    time.sleep(0.5)
    text2audio(text)


