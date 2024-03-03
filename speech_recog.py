import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Specify the audio file path
filename = "path/to/your/audio.wav"

# Load the audio file and convert speech to text
with sr.AudioFile(filename) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data)

print("Converted text:", text)
