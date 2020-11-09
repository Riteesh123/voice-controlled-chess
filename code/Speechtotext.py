import speech_recognition as sr
'''filename = "speech.wav"   # specific audio file to 
r = sr.Recognizer()

with sr.AudioFile(filename) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data)
    print(text)'''

r = sr.Recognizer()
print("Please Talk")
with sr.Microphone() as source:
    audio_data = r.record(source, duration=5)
    print("Recognising...")
    text = r.recognize_google(audio_data)
    print(text)