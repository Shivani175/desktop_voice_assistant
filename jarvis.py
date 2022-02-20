import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() #Without this command, speech will not be audible to us.



def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")
    else :
        speak("Good evening!")

    speak("I am zira. Please tell me how may  help you.")

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer() #recognizer class helps to recognixe output
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)
       

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query
    
if __name__ == "__main__":
    wishme()
    #while True:
    if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get('windows-default').open('http://www.youtube.com')

        elif 'open google' in query:
            webbrowser.get('windows-default').open('http://www.google.com')    

        elif 'play music' in query:
            music_dir = 'give the location of the folder where music is given'
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))  

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")  

        elif 'open vs code' in query:
            codePath = "C:\\Users\\Shivani14934\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)  

        