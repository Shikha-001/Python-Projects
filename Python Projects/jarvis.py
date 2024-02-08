# import pyjokes
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)    # change 1 to o in voice[1] to get output in male voice

def shutdown():
    os.system("shutdown /s /t 1")  # Shutdown after 1 second

def restart():
    os.system("shutdown /r /t 1")  # Restart after 1 second

def sleep():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")  # Put to sleep


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Log in to your Gmail account using the email address and password
    server.login('you@gmail.com', 'yourpasssword')
    server.sendmail('yourfriendmail@gmail.com', to, content)
    server.close()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
        print("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   
        print("Good Afternoon!") 

    else:
        speak("Good Evening!")  
        print("Good Evening!")  

    speak("I am Jarvis. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
  
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            try:
                speak('Searching Wikipedia...')
                query = query.replace('wikipedia', '')
                results = wikipedia.summary(query, sentences=2, auto_suggest=False)
                speak('According to Wikipedia')
                print(results)
                speak(results)
            except Exception as e:
                print(e)
                speak('Sorry, I could not find any results on Wikipedia.')


        elif "shutdown" in query:
            shutdown()
            break
        elif "restart" in query:
            restart()
            break
        elif "sleep" in query:
            sleep()
            break

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            print("Opening Youtube... ")

        elif 'open google' in query:
            webbrowser.open("google.com")
            print("Opening Google... ")

        elif 'open javatpoint' in query:
            webbrowser.open("https://www.javatpoint.com/")   
            print("Opening Javatpoint")


        elif 'play music' in query:
            music_dir = "C:/Users/USERNAME/Music"
            print("Opening Music")
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        elif 'open code' in query:
            codePath = "C:/Users/USERNAME/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Visual Studio Code/Visual Studio Code.lnk"
            print("Opening Visual Studio Code")
            os.startfile(codePath)
            #you should enter your path here

        # elif "joke" in query:
        #     joke_1 = pyjokes.get_joke(language="en",category="neutral")
        #     print(joke_1)
        #     speak(joke_1)

        elif 'quit' in query:
            speak("thankque")
            print("Thanque")
            speak("Have a nice day")
            print("Have a nice day")
            break



        
        if 'email to' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "yourfriend@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")