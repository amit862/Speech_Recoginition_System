import pyttsx3 #pip install pyttsx3
import datetime
import speech_recognition as sr # pip install speechRecogination
import wikipedia # pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui # pip install pyautogui
import psutil #pip install psutil
import pyjokes #pip install pyjokes 

from wikipedia.wikipedia import search

engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
# newVoiceRate = 150
# engine.setProperty('rate', newVoiceRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back sir!")
    hour = datetime.datetime.now().hour
    
    if hour >=6 and hour < 12:
        speak("Good morning")
    elif hour >=12 and hour < 18:
        speak("Good afternoon")
    elif hour >=18 and hour <=24:
        speak("good evening")
    else:
        speak("Good night")

    speak("Jarvis at your service. How I can help you?")

    

def takeCommand():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"

    return query

def sendmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com'), 587
    server.ehlo()
    server.starttls()
    server.login("amitverma09525@gmail.com", "123test")
    server.sendmail("amitverma09525@gmail.com", to, content)
    server.close()

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:/Users/sukant kumar verma/Desktop/python/Jarvis/ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage)

    battery = psutil.sensors_battery
    speak("battery is at")
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":

    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            speak(result)
        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "v20ami@gmail.com"
                # sendmail(to, content)
                speak("Email sent successfully")
            except Exception as e:
                speak(e)
                speak("Unable to send the message")
        elif "search in chrome" in query:
            speak("What should I search?")
            chromepath = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
        
        elif "logout" in query:
            os.system("shutdown -1")

        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r -1")

        elif "play songs" in query:
            songs_dir = "E:\songs"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))

        elif "remember that" in query:
            speak("What should i Remember?")
            data = takeCommand()
            speak("You should me to remember" + data)
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you know anything" in query:
            remember = open("data.txt", "r")
            speak("You said me to remember that" +remember.read())

        elif "screenshot" in query:
            screenshot()
            speak("Done!")
        
        elif "cpu" in query:
            cpu()

        elif "joke" in query:
            jokes()

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[0].id)
# newVoiceRate = 150
# engine.setProperty('rate', newVoiceRate)
# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# speak("Hello This is python assistant tutorial")