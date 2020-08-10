import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')#voices lene ke liye hum iss module ko use karte hai jo pehle se hi hai humare computer me.
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)#ladki ki voice set kardi


def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morning mr. vishal')#user use his name here 

    elif hour>=12 and hour<18:
        speak('good afternoon mr. vishal')

    else:
        speak('good evening mr. vishal')    

    speak('i am jarvis . please tell me how can i help  you')#greetings from jarvis

def takecommand():
    #it takes microphone input through user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening.....')
        r.pause_threshold = 1
        audio=r.listen(source)

        try:
            print('recognizing...')
            query= r.recognize_google(audio, language='en-in')
            print(f'user said:{query}\n')

        except Exception as e:
            #print(e)
            print('say that again please..')
            return "None"
        return query   

if __name__ == "__main__":
    #speak('vishal is a good boy')
    wishme()
    #while True:#leta rahega unlimited times
    if 1:#ek baar hi command lega
        query=takecommand().lower()

         #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak('according to wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stack overflow.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'play music' in query:
            music_dir= 'C:\\Users\\asus\\Desktop\\HD Song'
            songs=os.listdir(music_dir)
            #print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'sir , the time is {strTime}')

        elif 'open code' in query:
            code_path="C:\\Users\\asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)         



            
   
