from gtts import gTTS
#from subprocess import call     # MAC / LINUX
from playsound import playsound # WINDOWS

def cria_audios(audio):
    tts = gTTS('Oi, eu sou a Rose', lang='pt-br')
    tts.save('audios/audio')

    playsound('audios/audio.mp3')  # WINDOWS
    #call(['afplay', 'audios/audio.mp3']) # OSX
    #call(['aplay', 'audios/audio.mp3'])  # LINUX

cria_audios('Oi, eu sou a Rose.')