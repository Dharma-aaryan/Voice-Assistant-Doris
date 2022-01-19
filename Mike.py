#pip install pyttsx3
#pip install speechRecognition
#pip install wikipedia
#pip install PyAudio
#if there is an error in installing the PyAudio library, check the Readme file and refer the link given in the description and follow the steps

import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib

#sapi5 is a speech api that allows speech recognition
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#Mike will greet you 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
        
    elif hour >=12 and hour < 18:
        speak("Good Afternoon")
        
    else:
        speak("Good Evening")
        
    speak("Hello Sir\mam, I am your voice assistant, How can I help you today")

def takeCommand():
    #takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
            print("Listening")
            speak("Listening")
            r.pause_threshold = 1
            audio = r.listen(source)
            
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language = "en-ln")
        print(f"Query: {query}\n")
        
    except Exception as e:
        print("I didnt get that..")
        speak("I didnt get that")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("youremail@example.com", "password")
    server.sendmail("aaryan.dhams@gmail.com", to, content)
    server.close()
    
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if "what is your name" in query:
            speak("I am Mike your personal voice assistant")
            print("I am Mike your voice assistant")

        elif "what is your purpose" in query:
            speak("I am a simple voice-bot and here to help and assist you")
            print("I am a simple voice-bot and here to help and assist you")

        elif "what are the things that you can do" in query:
            speak("I can give you the time, open Youtube, Google and Wikipedia, play your favourite music, send email to your friends and search whatever you want on google and wikipedia")
            print("I can give you the time, open Youtube, Google and Wikipedia, play your favourite music, send email to your friends and search whatever you want on google and wikipedia")

        elif "open wikipedia" in query:
            speak("Opening wikipedia")
            webbrowser.open("wikipedia.com")
            
        elif "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia..")
            print(results)
            speak(results)

        elif "google" in query:
            speak("Searching google...")
            query = query.replace("google", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to google...")
            print(results)
            speak(results)
        
        elif "open youtube" in query:
            speak("Dont Spend too much time here")
            webbrowser.open("youtube.com")

        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("google.com")
            
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
            
        elif "play music" in query:
            music_dir = "yoursong.mp3"
            songs = os.listdr(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))    
            
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            
        elif "email to friend" in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to = "receiveremail@example.com"
                sendEmail(to, content)
                speak("Your Email has been seent!")
            except Exception as e:
                print(e)
                speak("Sorry I coulnt send the email")

        elif 'open code' in query:
            codePath = "Mike.py"
            os.startfile(codePath)

        elif "exit" in query:
            exit(0)
            
            
