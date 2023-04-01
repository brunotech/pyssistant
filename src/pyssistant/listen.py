import speech_recognition as sr

def listen(level=""):
    audio = None
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"{level}listening")
        audio = r.listen(source, phrase_time_limit=3)
        print(f"{level}thinking...")
    return audio

def lsiten_silently():
    audio = None
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, phrase_time_limit=3)
    return audio
