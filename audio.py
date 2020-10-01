
import pyaudio
import wave
import speech_recognition as sr
import subprocess
from commands import Commander


running = True


def echo(text):
    subprocess.call("PowerShell -Command Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('"+ text +"')", shell=True)


def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()
    
    stream = pa.open(
            format = pa.get_format_from_width(wf.getsampwidth()),
            channels = wf.getnchannels(),
            rate = wf.getframerate(),
            output = True
    )
    
    data_stream = wf.readframes(chunk)
    
    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)
        
    stream.close()
    pa.terminate()
    
#play_audio("./audio/Fart.wav")
    
r = sr.Recognizer()
cmd = Commander()

def initSpeech():
    print("Listening .... ")
    
    
    play_audio("./audio/audio1.wav")
    
    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)
        
    play_audio("./audio/audio1.wav")
    
    command = ""
    
    try:
        command = r.recognize_google(audio)
        
    except:
        print("Couldn't understand you, bro.")
        
    print("Your Command: ")
    print(command)
    if command == "quit":
        running = False
        
    cmd.discover(command)
    #echo('You said: ' + command)    #   change speak to say ********
    
    
while running == True:
    initSpeech()