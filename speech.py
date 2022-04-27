import speech_recognition as sr
import pyttsx3
import os
import keyboard
import subprocess
import psutil


recognizer = sr.Recognizer()

while True:
    try:

        with sr.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio, language='RU', ).lower()
            print(f"Recognized: {text}")

            if text == 'открой спотифай' or text == 'открой spotify':
                subprocess.call(r'C:\Users\glazo\AppData\Roaming\Spotify\Spotify.exe')
            if text == 'закрой спотифай' or text == 'закрой spotify':
                for process in (process for process in psutil.process_iter() if process.name() == "Spotify.exe"):
                    process.kill()

            if text == 'открой телеграм' or text == 'открой telegram':
                subprocess.call(r'C:\Workspace\Telegram Desktop\Telegram.exe')
            if text == 'закрой телеграм' or text == 'закрой telegram':
                for process in (process for process in psutil.process_iter() if process.name() == "Telegram.exe"):
                    process.kill()


    except sr.UnknownValueError:
        recognizer = sr.Recognizer()
        continue
