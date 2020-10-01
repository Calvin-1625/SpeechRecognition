import subprocess
import os

class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "si", "do it", "yeah", "confirm"]
        self.cancel = ["no", "negative", "negative soldier", "don't", "wait", "cancel"]
        
    def discover(self, text):
        if "what" in text and "your name" in text:
            if "my" in text:
                self.respond("You haven't told me your name yet")
            else:
                self.respond("My name is python commander. How are you?")
                
    def respond(self, response):
        print(response)
        subprocess.call("PowerShell -Command Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('" + response + "')", shell=True)