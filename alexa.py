import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_cmd():
    try:
        with sr.Microphone() as source:
            print("listening.....")
            voice = listener.listen(source)
            cmd = listener.recognize_google(voice)
            cmd = cmd.lower()
            if "alex" in cmd: 
                cmd = cmd.replace("alex", "")
                print(cmd)           
                # talk(cmd)  
            else: 
                talk("Please Say something I can understand!")
    except:
        pass
    return cmd

def run_alex():
    cmd = take_cmd()
    # print (cmd)
    if "play" in cmd:
        song = cmd.replace("play", "")
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif "time" in cmd:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        talk("Current time is" + time)

    elif "hey" or "hello" or "hi" in cmd:
        talk("What can I do for you")

    elif "who"  in cmd:
        person = cmd.replace("who", "")
        info = wikipedia.summary(person,1)
        print (info)
        talk (info)

    elif "date" in cmd:
        talk("Sorry, I have a headache")

    elif "single" in cmd:
        talk ("Sorry, but I am already in a relation with wifi!")

    elif "friend" in cmd:
        talk("Yesss, I am always there for you!")

    elif "joke" in cmd:
        humour = pyjokes.get_joke()
        print (humour)
        talk(humour)

    elif "bye" in cmd:
        talk("bye!")
        exit
    
    else:
        talk("Please Say something I can understand!")

while True:
    run_alex()