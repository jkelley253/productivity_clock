import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')

for index, voice in enumerate(voices):
    print(f"voice {index}")
    print(f" - ID: {voice.id}")
    print(f" - Name: {voice.name}")
    print(f" - language: {voice.name}")
    print(f" - Gender: {'Male' if 'male' in voice.name.lower() else 'Famale'}")
    print("-" * 30)