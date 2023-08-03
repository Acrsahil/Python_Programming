from asyncio import Task
import os
import speech_recognition as sr
import webbrowser
import pyttsx3
from gtts import gTTS
import playsound
import webbrowser
import pywhatkit
from playsound import playsound
import wikipedia
import pyautogui
import pyttsx3
import keyboard
import datetime
from playsound import playsound
import pyjokes
from PyDictionary import PyDictionary as Diction
from tkinter import *

from tkinter import Tk
from PIL import Image, ImageTk
gui = Tk()


def speak(text):
    print(" ")
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    print(f": {text}")
    print("  ")
    playsound("output.mp3")
    os.remove("output.mp3")

    # Assistant.say(audio)
    # print(" ")
    # print(f":{audio}")
    # Assistant.runAndWait()
 # Adjust the speech volume, default is 1.0

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(" ")
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language="en-in")
        print(" ")
        print(f"User said: {query}")
        return query
    except Exception as Error:
        return "None"


def TaskExe():
    speak("Hello sir, I am Jarvis!")

    def Watsapp():
        speak("Tell me the name of the person!")
        name = takeCommand()

        if 'sugam' in name or 'Sugam' in name:
            speak("Tell me the message!")
            msg = takeCommand()
            speak("Tell me the time, sir!")
            speak("Time in hour!")
            hour = int(takeCommand())
            speak("Time in minutes")
            min = int(takeCommand())
            pywhatkit.sendwhatmsg("+9779816060212", msg, hour, min, 20)
            speak("OK Sir, sending WhatsApp message")
        elif 'Nishal' in name or 'nishal' in name:
            speak("Tell me the message!")
            msg = takeCommand()
            speak("Tell me the time, sir!")
            speak("Time in hour!")
            hour = int(takeCommand())
            speak("Time in minutes")
            min = int(takeCommand())
            pywhatkit.sendwhatmsg("+9779801927183", msg, hour, min, 20)
            speak("OK Sir, sending WhatsApp message")
        elif 'Mum' in name or 'mum' in name:
            speak("Tell me the message!")
            msg = takeCommand()
            speak("Tell me the time, sir!")
            speak("Time in hour!")
            hour = int(takeCommand())
            speak("Time in minutes")
            min = int(takeCommand())
            pywhatkit.sendwhatmsg("+9779807936028", msg, hour, min, 20)
            speak("OK Sir, sending WhatsApp message")
        elif 'Tenzin' in name or 'tenzin' in name:
            speak("Tell me the message!")
            msg = takeCommand()
            speak("Tell me the time, sir!")
            speak("Time in hour!")
            hour = int(takeCommand())
            speak("Time in minutes")
            min = int(takeCommand())
            pywhatkit.sendwhatmsg("+9779762285689", msg, hour, min, 20)
            speak("OK Sir, sending WhatsApp message")
        elif 'Babu' in name or 'Baba' in name or 'Dad' in name:
            speak("Tell me the message!")
            msg = takeCommand()
            speak("Tell me the time, sir!")
            speak("Time in hour!")
            hour = int(takeCommand())
            speak("Time in minutes")
            min = int(takeCommand())
            pywhatkit.sendwhatmsg("+9779851177355", msg, hour, min, 20)
            speak("OK Sir, sending WhatsApp message")

    def Vajan():
        speak("Tell me the name of the bhaajan!")
        musicName = takeCommand()

        if 'bhakti' in musicName or 'bhakti dance' in musicName or 'bhakti dan' in musicName:
            playsound("/home/dassahil/Desktop/jagatguru-rampal-ji/vajan/05 Bhakti dan guru dijiyo.mp3")
        elif 'upar' in musicName or 'uper' in musicName or 'apa' in musicName or 'upper' in musicName:
            playsound("/home/dassahil/Desktop/jagatguru-rampal-ji/vajan/01 The uper ne pair.mp3")
        elif 'Main To pavega'in musicName or 'man to pawaga' in musicName or 'main to pawagea' in musicName or 'man' in musicName or 'pawaga' in musicName:
            playsound("/home/dassahil/Desktop/jagatguru-rampal-ji/02  Man tu pawega apna kiya re.mp3")
        else:
            pywhatkit.playonyt(musicName)

        speak("Your search has been started from the Youtube Enjoy!")
    
    def YoutubeAuto():
        speak("Whats Your Command ?")
        comm = takeCommand()

        if 'pause' in comm:
            keyboard.press('space bar')
        elif 'restart' in comm:
            keyboard.press('0')
        
        elif 'mute' in comm:
            keyboard.press('m')
        elif 'skip' in comm:
            keyboard.press('l')
        elif 'back' in comm:
            keyboard.press('j')
        elif 'full screen' in comm:
            keyboard.press('f')
        elif 'film mode' in comm:
            keyboard.press('t')
        speak("Done Sir!")
    
    def braveAuto():
        speak("Chrome Automation started!")
        command = takeCommand()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + shift + w')
        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')
        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')
        elif 'history' in command:
            keyboard.press_and_real ('ctrl + h')
        elif 'downloads' in command:
            keyboard.press_and_real ('ctrl + j')
        elif 'bookmark this page' in command:
            keyboard.press_and_release('ctrl + d')
        elif 'turn to full screen' in command:
            keyboard.press_and_release('f11')
        
    def Dict():
        speak("Tell me the problem!")
        speak("Activated Dictionary!")
        probl = takeCommand()

        if 'meaning' in probl:
            probl = probl.replace("what is the", "")
            probl = probl.replace("meaning of", "")
            probl = probl.replace("jarvis", "")
            probl = probl.replace("of", "")
            probl = probl.strip()  # Remove leading/trailing spaces
            dictionary = Diction()
            result = dictionary.meaning(probl)
            speak(f"The meaning of {probl} is {result}")
        elif 'synonym' in probl:
            probl = probl.replace("what is the", "")
            probl = probl.replace("synonyms of", "")
            probl = probl.replace("jarvis", "")
            probl = probl.replace("of", "")
            probl = probl.strip()  # Remove leading/trailing spaces
            dictionary = Diction()
            result = dictionary.synonym(probl)
            speak(f"The synonym of {probl} is {result}")
        elif 'antonym' in probl:
            probl = probl.replace("what is the", "")
            probl = probl.replace("antonym of", "")
            probl = probl.replace("jarvis", "")
            probl = probl.replace("of", "")
            probl = probl.strip()  # Remove leading/trailing spaces
            dictionary = Diction()
            result = dictionary.antonym(probl)
            speak(f"The antonym of {probl} is {result}")

        speak("Exited Dictionary!")
    
    def TakeHindi():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print(" ")
            print("Listening.....")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing.....")
            query = r.recognize_google(audio, language="hi")
            print(" ")
            print(f"User said: {query}")
            return query
        except Exception as Error:
            return "None"
    def Tran():
        speak("Tell Me the Line!")
        line = TakeHindi()
            
    while True:
        query = takeCommand()

        if 'hello' in query:
            speak("Hello Sir, I am Mimi.")
            speak("Your personal AI Assistant!")
            speak("How may I help you?")
        elif 'how are you' in query:
            speak("I am fine, thank you.")
            speak("What about you?")
        elif 'you need a break' in query:
            speak("OK Sir, you can call me anytime!")
            break
        elif 'bye' in query or 'By' in query or 'by' in query:
            speak("OK Sir, Bye!")
            break
        elif 'youtube search' in query.lower():
            speak("OK Sir, this is what I found for your search")
            query = query.replace("youtube search", "")
            query = query.replace("jarvis ", "")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            speak("Done Sir!")
        elif 'google search' in query.lower():
            speak("This is what I found for your search!")
            query = query.replace("google search", "")
            query = query.replace("jarvis", "")
            pywhatkit.search(query)
            speak("Done Sir!")
        elif 'website' in query:
            speak("OK Sir, launching.....")
            web1 = query.replace("open", "")
            web1 = web1.replace("jarvis", "")
            web1 = web1.replace("website", "")
            web1 = web1.replace(" ","")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)

        elif 'launch' in query:
            speak("Tell me the name of the website!")
            name = takeCommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            speak("Done Sir!")
        elif 'vajan' in query or 'bhajan' in query:
            Vajan()
        elif 'wikipedia' in query or 'Wikipedia' in query:
            speak("Searching Wikipedia.....")
            query = query.replace("Wikipedia", "")
            query = query.replace("wikipedia", "")
            try:
                wiki = wikipedia.summary(query, 2)
                speak(f"According to Wikipedia: {wiki}")
            except wikipedia.exceptions.PageError:
                speak("Sorry, I couldn't find any relevant information on Wikipedia.")
            except wikipedia.exceptions.DisambiguationError:
                speak("There are multiple options available. Please provide a more specific query.")
        elif 'watsapp message' in query or 'Watsapp message' in query or 'WhatsApp message' in query:
            Watsapp()
        elif 'screenshot' in query:
            kk = pyautogui.screenshot()
            kk.save('/home/dassahil/Pictures/screenshot.png')



        # application open
        elif 'open brave' in query or 'open Brave' in query:
            os.system("/home/dassahil/Desktop/brave-browser.desktop")


        # website opening
        elif "open YouTube" in query or "open youtube" in query:
            speak("OK Sir, wait a second")
            webbrowser.open("https://www.youtube.com")
            speak("Your command has been completed, Sir!")

        elif "open leetcode" in query or "open Leetcode" in query or "lit code" in query or "Leet code" in query:
            speak("OK Sir, wait a second")
            webbrowser.open("https://leetcode.com")
            speak("Your command has been completed, Sir!")

        elif "open wikipedia" in query or "open Wikipedia" in query:
            speak("OK Sir, wait a second")
            webbrowser.open("https://www.wikipedia.org")
            speak("Your command has been completed, Sir!")

        elif "open gmail" in query or "open Gmail" in query:
            speak("OK Sir, wait a second")
            webbrowser.open("https://mail.google.com")
            speak("Your command has been completed, Sir!")

        elif "open keybr" in query or "open KBR" in query or "open KVR" in query or "open Keybr" in query:

            speak("OK Sir, wait a second")
            webbrowser.open("https://www.keybr.com")
            speak("Your command has been completed, Sir!")
        elif "open linkedin" in query or "open Linkedin" in query or "open LinkedIn" in query:

            speak("OK Sir, wait a second")
            webbrowser.open("https://www.linkedin.com")
            speak("Your command has been completed, Sir!")
        elif 'pause' in query:
            keyboard.press('space bar')
        elif 'restart' in query:
            keyboard.press('0')
        
        elif 'mute' in query:
            keyboard.press('m')
        elif 'skip' in query:
            keyboard.press('l')
        elif 'back' in query:
            keyboard.press('j')
        elif 'full screen' in query:
            keyboard.press('f')
        elif 'film mode' in query:
            keyboard.press('t')
            speak("Done Sir!")
        elif 'youtube tool' in query or 'YouTube Tool' in query or 'YouTube tool' in query:
            YoutubeAuto() 

        elif 'close this tab' in query:
            keyboard.press_and_release('ctrl + shift + w')
        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')
        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')
        elif 'history' in query:
            keyboard.press_and_real ('ctrl + h')
        elif 'downloads' in query:
            keyboard.press_and_real ('ctrl + j')
        elif 'bookmark this page' in query:
            keyboard.press_and_release('ctrl + d')
        elif 'turn to full screen' in query:
            keyboard.press_and_release('f11')
        elif 'brave automation' in query:
            braveAuto()
        elif 'joke' in query:
            get = pyjokes.get_joke()
            speak(get)
        elif 'repeat my words' in query:
            speak("Speak Sir!")
            jj = takeCommand()
            speak(f"You said :{jj}")
        elif 'my location' in query:
            speak("Ok Sir , Wait A Second!")
            webbrowser.open('https://www.google.com/maps/@27.7419997,85.2694121,13.21z?entry=ttu')
        elif 'dictionary' in query:
            Dict()
        elif 'alarm' in query or 'Alarm' in query or 'alaarm' in query:
            speak("Enter The time !")
            time = input(": Enter The Time :")

            while True:
                Time_Ac = datetime.datetime.now()
                print(Time_Ac)
                now = Time_Ac.strftime("%H:%M:%S")
                print(Time_Ac.strftime("%H:%M:%S"))

                if now == time:
                    speak("Time To Wake Up Sir!")
                    playsound('alarm.mp3')
                    speak("Alarm Closed!")
                    
                elif now>time:
                    break

            

        elif not query:
            continue
        
        else:
            speak("Sorry, I couldn't understand the query.")

def start():
    TaskExe()


gui.minsize(height=800, width=1270)
gui.maxsize(height=800,width=1270)
gui.title('Jarvis')
img =Image.open('jarvisbg.png') 
bg = ImageTk.PhotoImage(img)
label = Label(gui, image=bg)
label.place(x = 0,y = 0)


# Try setting the window icon with a PNG or GIF image file (icon.png)
# image_path = 'i.ico'
# image = Image.open(image_path)
# Adjust the desired size of the image
new_width = 200
new_height = 200
# image = image.resize((new_width, new_height), Image.BILINEAR)
# image = ImageTk.PhotoImage(image)
# image_label = Label(gui, image=image)
# image_label.pack(pady=10)
results_label = Label(gui, text="",height=12, justify=LEFT, font=('Arial', 12))
results_label.pack(pady=10)
gui.attributes("-alpha", 0.0)

# Create the button with transparent background
show_passwords_button = Button(gui, text="Run Jarvis", command=start, height=12, width=25, bd=0, highlightthickness=0)

# Pack the button
show_passwords_button.pack()



gui.mainloop()










