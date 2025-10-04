import time

import speech_recognition as sr

from command_handlers import *
from silence_alsa import silence_alsa

hotword = "hey assistant"
commands = {"search": search_handler, "stop": stop_handler, "chrome 2": chrome2_handler}

def speech_handler(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language="en-US").lower()
        print(f"You said: {text}")
        if text.startswith(hotword):
            command = text[len(hotword):].strip()
            print(f"Command detected: {command}")

            for key in commands:
                if command.startswith(key):
                    arg = command[len(key):].strip()
                    commands[key](arg)
                    break

    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print(f"API error: {e}")


if __name__ == "__main__":
    silence_alsa()

    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    # Start listening in the background
    stop_listening = recognizer.listen_in_background(mic, speech_handler)

    print("Listening in background... Press Ctrl+C to stop.")

    while True:
        time.sleep(20000)  # keep the main thread alive
