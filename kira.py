import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import subprocess, sys

engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+50)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Kira. May I help you?")       

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source,duration=1)
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:   
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ankursinghgdr@gmail.com', 'yourPassword')
    server.sendmail('yourEmail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
     if 1:
       
        # chrome_path ='/Users/Kira/Desktop/Google Chrome'
        # browser=webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
        # print (webbrowser._browsers)
        query = takeCommand().lower()
#         # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results) 
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get('safari').open("http://youtube.com")

        elif 'open google' in query:
            webbrowser.get('safari').open("http://google.com")

        elif 'open stack overflow' in query:
            webbrowser.get('safari').open("http://stackoverflow.com")   


        elif 'play music' in query:
            music_dir = '/Users/Kira/Desktop/projects/songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")


        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "yourEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir, some error occured. I am not able to send this email")    