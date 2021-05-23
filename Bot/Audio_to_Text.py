import speech_recognition as sr
import webbrowser

r1=sr.Recognizer()

with sr.Microphone() as source:
    print("hi")
    audio=r1.listen(source)
    try:
        text=r1.recognize_google(audio)
        print('{}'.format(text))
    except:
        print("sorry!")
