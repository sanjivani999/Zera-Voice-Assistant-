import pyttsx3
import speech_recognition as sr
import datetime
from time import sleep
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import time
import pyautogui
from keyboard import press
import pyjokes
import requests
import instaloader
import PyPDF2
from gtts import gTTS
from googletrans import Translator
import googletrans
#from bs4 import beautifulsoup4
from pywikihow import search_wikihow
from playsound import playsound
import speedtest
import json
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_MainWindow
from plyer import notification
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import timezone
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import exit





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


#to convert voice into text
def takecommand(self):
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source) #,timeout=5,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said; {query}")
      

    except Exception as e:
        speak("sir, i am not able to hear you. say that again please...")
        return "none"
    return query 

#for wakeup jarvis
def takecommandforwakeup(self):
    
    r =sr.Recognizer()
    with sr.Microphone() as source:
        
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source) #,timeout=5,phrase_time_limit=5)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said; {query}")
      
    except Exception as e:
        return "none"
    return query

#for every funtction
def takecommandkkk(self):
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source) #,timeout=5,phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said; {query}")
      

    except Exception as e:
        speak("sir, i am not able to hear you. say that again please please please...")
        return "none"
    return query   


        
                            

#to wish
def wish():

    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am zira sir. how can i help you")  

class Mainthread(QThread):
    def __init__(self):
        super(Mainthread,self).__init__()

    def run(self):
        self.TaskExecution()


# to send email
def sendEmail(to, sub, mess,):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('dhordekunal@gmail.com', 'pjmzvnqerrbayytl')
    server.sendmail('dhordekunal@gmail.com', to, sub, mess)
    server.close()
    
          


class Mainthread(QThread):
    def __init__(self):
        super(Mainthread,self).__init__()

    def run(self):
        self.TaskExecution()    
       
    def takecommand(self):
        r =sr.Recognizer()
        with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1
         audio = r.listen(source) #,timeout=5,phrase_time_limit=5)

        try:
         print("Recognizing...")
         query = r.recognize_google(audio, language='en-in')
         print(f"user said; {query}")
      

        except Exception as e:
         speak("sir, i am not able to hear you. say that again please...")
         return "none"
        return query

        #for kkkkkk
    def takecommandkkk(self):
        while True:

            r =sr.Recognizer()
            with sr.Microphone() as source:
             print("Listening...")
             r.pause_threshold = 1
             audio = r.listen(source) #,timeout=5,phrase_time_limit=5)

            try:
             print("Recognizing...")
             query = r.recognize_google(audio, language='en-in')
             print(f"user said; {query}")
        

            except Exception as e:
             speak("sir, i am not able to hear you. say that again please...")
             return "none"
            return query
 
    #for wakeup jarvis
    def takecommandforwakeup(self):
        
        r =sr.Recognizer()
        with sr.Microphone() as source:
            
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source) #,timeout=5,phrase_time_limit=5)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said; {query}")
        
        except Exception as e:
            return "none"
        return query


    

    #if __name__ == "__main__":
    def TaskExecution(self):
              

        wish()
        #takecommand()
        #speak("hello sir")
        while True:
         if 1: 

            self.query = self.takecommand()
            

            #logic building for tasks

            if "open Notepad" in self.query:
                speak("opening notepad")
                #npath = "C:\\Users\\HP\\OneDrive\\Desktop\\Notepad.lnk"
                npath = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2210.5.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe"
                os.startfile(npath)
                speak("sir, notepad as open successfully")
            elif "close notepad" in self.query:
                speak("ok sir, closing  notepad")
                os.system(f"taskkill /f /im Notepad.exe")
                speak("sir, notepad has been closed successfully") 

            #############  youtube Automation   #############
            #################################################
            #elif("take screenshot")  in self.query or ("take a screenshot")  in self.query:
            elif "open YouTube" in self.query or "Open YouTube" in self.query or "open the YouTube" in self.query or "Open the YouTube" in self.query :
                speak("opening youtube")
                webbrowser.open("www.youtube.com")
                speak(" sir, what you would like to search?") 
                am = self.takecommand().lower()
                speak("sir, here are some result's you are looking for")
                kit.playonyt(am)
                time.sleep(4)
                pyautogui.press("space")

            elif "YouTube search" in self.query:
                speak("sir, what would you will like to search") 
                yt = self.takecommand().lower()
                speak("ok sir, searching"+ (yt))
                time.sleep(1)
                pyautogui.click(458,131)
                pyautogui.typewrite(yt)
                pyautogui.press("enter")
                speak("sir, here is the result you are looking for")   

            elif "video number 1" in self.query:
                speak("ok sir, opening vedio") 
                pyautogui.click(395,275)
                speak("sir, video is open")

            elif "video number 2" in self.query:
                speak("ok sir, opening vedio") 
                pyautogui.click(393,510)
                speak("sir, video is open")

            elif "video number 3" in self.query:
                speak("ok sir, opening vedio") 
                pyautogui.click(393,679)
                speak("sir, video is open")          

            elif "refresh" in self.query:
                pyautogui.press("F5")
                speak("sir, you have successfully refresh the page") 

            elif "enter" in self.query:
                pyautogui.press("enter")
                speak("sir, you have successfully press enter")

            elif "stop" in self.query:
                pyautogui.press("space")
                speak("sir, you have successfully paused the musics")

            elif "play the video" in self.query or "play video" in self.query:
                pyautogui.press("space")    
                speak("sir, you have successfully played the video")

            elif "next" in self.query:
                pyautogui.keyDown("Shift")
                press("n")
                pyautogui.keyUp("Shift")
                speak("sir, you have successfully played next") 

            elif "previous" in self.query:
                pyautogui.keyDown("Shift")
                press("p")
                pyautogui.keyUp("Shift")
                speak("sir, you have successfully played previous vedio") 
 
            elif "mute video" in self.query or "mute the fvideo" in self.query:
                press("m")
                speak("sir, you have successfully muted video") 

            elif "increase video volume" in self.query or "increase  the video volume" in self.query:
                pyautogui.press("up")
                speak("sir, volume is increase by 5 percent")

            elif "decrease video volume" in self.query or "decrease the video volume" in self.query:
                pyautogui.press("down")
                speak("sir, volume is decrease by 5 percent")    

            elif "full screen" in self.query:
                press("f")
                speak("sir, full screen is done")

            elif "continue video" in self.query or "continue the video" in self.query:
                press("i")
                speak("sir, continued vedio")

            elif "go back" in self.query:
                pyautogui.keyDown("alt")
                press("left")
                pyautogui.keyUp("alt")
                speak("sir, you have goan one step back")    

            elif "escape" in self.query or "excape" in self.query:
                press("ESCAPE")
                speak("sir, you have successfully pressed Escape")

            elif "40%" in self.query:
                press("4")
                speak("sir, video is skip by forty percent")     

            elif "keep video" in self.query or "skip video" in self.query or "skip the video" in self.query:
                press("l")
                speak("sir, vedio is skip")

            elif "keep back" in self.query or "skip back" in self.query:
                press("j")
                speak("sir, vedio is skip back")  

            elif "from start" in self.query or "from the start" in self.query:
                press("0")
                speak("sir, vedio is played from start")

            elif "on subtitles" in self.query or "on the subtitles" in self.query:
                press("c")
                speak("sir, subtitles is on")

            elif "of the subtitles" in self.query:
                press("c")
                speak("sir, subtitles is off") 

            elif "ZoomIn" in self.query or "zoom in" in self.query:
                pyautogui.keyDown("win")
                press("+")
                pyautogui.keyUp("win")
                speak("sir, you have zoom in")

            elif "zoom out" in self.query:
                pyautogui.keyDown("win")
                press("-")
                pyautogui.keyUp("win")
                speak("sir, you have zoom out")                            

            #############  chrome Automation   #############
            #################################################               
            elif "open Chrome" in self.query or "open the Chrome" in self.query:
                speak("opening chrome")
                npath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(npath)
                speak("sir, chrome as open successfully")

            elif "close Chrome" in self.query or "close the Chrome" in self.query:
                speak("ok sir, closing  chrome")
                os.system(f"taskkill /f /im chrome.exe")
                speak("sir, chrome has closed successfully")

            elif "close browser" in self.query or "close the browser" in self.query:
                speak("ok sir, closing browser")  
                pyautogui.keyDown("Ctrl")
                pyautogui.press("w")
                pyautogui.keyUp("Ctrl")     
                speak("sir, you have successfully closed browser") 

            elif "Browser search" in self.query:
                speak("ok sir, what would you like to search")
                go = self.takecommand().lower()
                speak("sir searching " + (go))
                pyautogui.typewrite(go)
                pyautogui.press("enter")
                speak("sir, here are the result you are looking for")

            elif "switch window" in self.query or "switch the window" in self.query:
                speak('ok sir, switching the window')
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                pyautogui.keyUp("alt")     
                speak("sir, you have successfully switched the window")

            elif "show all Windows" in self.query or "show all the windows" in self.query:
                speak("ok sir")        
                pyautogui.keyDown("win")
                pyautogui.press("tab")
                pyautogui.keyUp("win")
                time.sleep(1)
                speak("sir, here are the all windows which are currently running") 

            elif "window 2" in self.query:
                speak("ok sir, opening second window")
                pyautogui.press("right") 
                pyautogui.press("enter")
                speak("sir, second window is open successfully")

            elif "window 3" in self.query:
                speak("ok sir, opening third window")
                pyautogui.press("right", presses=2) 
                pyautogui.press("enter")
                speak("sir, third window is open successfully")

            elif "window 4" in self.query:
                speak("ok sir, opening fourth window")
                pyautogui.press("right", presses=3) 
                pyautogui.press("enter")
                speak("sir, fourth window is open successfully")        

            elif "window 5" in self.query:
                speak("ok sir, opening fifth window")
                pyautogui.press("right", presses=4) 
                pyautogui.press("enter")
                speak("sir, fifth window is open successfully")

            elif "window 6" in self.query:
                speak("ok sir, opening sixth window")
                pyautogui.press("right", presses=5) 
                pyautogui.press("enter")
                speak("sir, sixth window is open successfully")

            elif "window 7" in self.query:
                speak("ok sir, opening seventh window")
                pyautogui.press("right", presses=6) 
                pyautogui.press("enter")
                speak("sir, seventh window is open successfully")

            elif "window 8" in self.query:
                speak("ok sir, opening eight window")
                pyautogui.press("right", presses=7) 
                pyautogui.press("enter")
                speak("sir, eight window is open successfully")

            elif "window 9" in self.query:
                speak("ok sir, opening ninth window")
                pyautogui.press("right", presses=8) 
                pyautogui.press("enter")
                speak("sir, ninth window is open successfully")

            elif "window 10" in self.query:
                speak("ok sir, opening tenth window")
                pyautogui.press("right", presses=9) 
                pyautogui.press("enter")
                speak("sir, tenth window is open successfully")

            elif "close application" in self.query or "close the application" in self.query or "exit application" in self.query or "exit current application" in self.query:
                speak("ok sir,closing current application")    
                pyautogui.keyDown("win")
                pyautogui.press("tab")
                pyautogui.keyUp("win")
                pyautogui.press("Delete")
                pyautogui.keyDown("win")
                pyautogui.press("d")
                pyautogui.keyUp("win")
                speak("sir, your current application is closed successfully")

            elif "close all windows" in self.query:
                speak("ok sir,closing all windows which are currently running")        
                pyautogui.keyDown("Alt")
                pyautogui.press("tab")
                pyautogui.press("Delete")
                time.sleep(1)
                pyautogui.press("Delete")
                time.sleep(1)
                pyautogui.press("Delete")
                time.sleep(1)
                pyautogui.press("Delete")
                time.sleep(1)
                pyautogui.press("Delete")
                time.sleep(1)
                pyautogui.press("Delete")
                time.sleep(1)
                pyautogui.press("Delete")
                pyautogui.keyUp("Alt")
            
            elif "maximize window" in self.query or "maximize the window" in self.query:
                speak("ok sir, maximizing window")        
                pyautogui.keyDown("win")
                pyautogui.press("up")
                pyautogui.keyUp("win")
                speak("sir, you have successfully maximize window")   

            elif "new tab" in self.query:
                speak("ok sir, opening new tab")        
                pyautogui.keyDown("Ctrl")
                press("T")
                pyautogui.keyUp("Ctrl")
                speak("sir, you have successfully created new tab")
                #speak("sir, would like to search something please tell YES or NO")
                #rr= self.takecommand()
                #if "yes" in rr:
                #    speak("sir, what would you like to search")
                #    rr= self.takecommand()
                #    speak("sir searching " + (rr))
                #    pyautogui.typewrite(rr)
                #    pyautogui.press("enter")
                #    speak("sir, here are the result you are looking for")
                #elif "no" in rr:
                #    speak("ok sir")
                #    pass   

            elif "new browser" in self.query:
                speak("ok sir, opening new browser")        
                pyautogui.keyDown("Ctrl")
                press("n")
                pyautogui.keyUp("Ctrl")
                speak("sir, you have successfully created new browser")    


            elif "Close tab" in self.query or "close the tab" in self.query or "close the tab" in self.query:
                speak("ok sir, closing tab")        
                pyautogui.keyDown("Ctrl")
                press("W")
                pyautogui.keyUp("Ctrl")
                speak("sir, you have successfully closed tab")

            elif "tab number 1" in self.query:
                speak("ok sir, opening tab one")        
                pyautogui.keyDown("Ctrl")
                press("1")
                pyautogui.keyUp("Ctrl")
                speak("sir, you have successfully open tab one")

            elif "tab number 2" in self.query:
                speak("ok sir, opening tab two")        
                pyautogui.keyDown("Ctrl")
                press("2")
                pyautogui.keyUp("Ctrl")
                speak("sir, you have successfully open tab two")  

            elif "tab number 3" in self.query:
                speak("ok sir, opening tab one")        
                pyautogui.keyDown("Ctrl")
                press("3")
                pyautogui.keyUp("Ctrl")
                speak("sir, you have successfully open tab three") 

            elif "tab number 4" in self.query:
                speak("ok sir, opening tab four")        
                pyautogui.keyDown("Ctrl")
                press("4")
                pyautogui.keyUp("Ctrl")
                speak("sir, you have successfully open tab four")  

            elif "tab number 5" in self.query:
                speak("ok sir, opening tab five")        
                pyautogui.keyDown("Ctrl")
                press("5")
                pyautogui.keyUp("Ctrl")
                speak("sir, you have successfully open tab five")  

            elif "tab number 6" in self.query:
                speak("ok sir, opening tab six")        
                pyautogui.keyDown("Ctrl")
                press("6")
                pyautogui.keyUp("Ctrl")
                speak("sir, you have successfully open tab six") 

            elif "tab number 7" in self.query:
                speak("ok sir, opening tab seven")        
                pyautogui.keyDown("Ctrl")
                press("7")
                pyautogui.keyUp("Ctrl")
                speak("sir, you have successfully open tab seven")   

            elif "tab number 8" in self.query:
                speak("ok sir, opening tab one")        
                pyautogui.keyDown("Ctrl")
                press("8")
                pyautogui.keyUp("Ctrl")
                speak("sir, you have successfully open tab eight")  

            elif "tab number 9" in self.query:
                speak("ok sir, opening tab eight")        
                pyautogui.keyDown("Ctrl")
                press("9")
                pyautogui.keyUp("Ctrl")
                speak("sir, you have successfully open tab eight")                   

            elif "switch the tab" in self.query or "switch tab" in self.query:
                speak("ok sir, shifting tab")        
                pyautogui.keyDown("Ctrl")
                pyautogui.press("Tab")
                pyautogui.keyUp("Ctrl")
                speak("sir, you have successfully shifted tab")

            elif "download page" in self.query:
                speak("ok sir, opening download page")        
                pyautogui.keyDown("Ctrl")
                press("j")
                pyautogui.keyUp("Ctrl")
                speak("sir, here is download page") 

            elif "find word" in self.query or "find the word" in self.query:
                speak("ok sir")        
                pyautogui.keyDown("Ctrl")
                press("f")
                pyautogui.keyUp("Ctrl")
                speak("sir, which word you will like to find")  
                f=self.takecommand().lower()
                speak("sir, please wait a second")
                speak("finding " + (f))
                pyautogui.typewrite(f)
                time.sleep(2)
                speak("sir, you have successfully finded " + (f)) 

            elif "reload page" in self.query or "reload the page" in self.query:
                speak("ok sir")        
                pyautogui.press("F5")
                speak("sir, you have reloaded page") 

            elif "scroll up" in self.query:
                speak("ok sir")        
                pyautogui.press("PageUp")
                speak("sir, you have scroll up")        

            elif "scroll down" in self.query:
                speak("ok sir")        
                pyautogui.press("PageDown")
                speak("sir, you have scroll down") 

            elif "open Microsoft Browser" in self.query:
                speak("opening microsoft browser")
                npath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                os.startfile(npath)   
                speak("sir, microsoft browser as open successfully") 
            elif "close Microsoft Browser" in self.query:
                speak("ok sir, closing microsoft browser")
                os.system(f"taskkill /f /im msedge.exe")
                speak("sir, microsoft browser   has been closed successfully")        

            #############  whatsapp Automation   #############
            #################################################
            elif "open WhatsApp" in self.query:
                speak("opening whatsapp")
                npath = "C:\\Users\\HP\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
                os.startfile(npath) 
                speak("sir, whatsapp as open successfully")
            elif "close WhatsApp" in self.query or "exit WhatsApp" in self.query:
                speak("ok sir, closing  whatsapp")
                os.system(f"taskkill /f /im WhatsApp.exe")
                speak("sir, whatsapp has been closed successfully")

            elif "open chat" in self.query or "open the chat" in self.query:
                npath = "C:\\Users\\HP\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
                os.startfile(npath) 
                speak("opening whatsapp chat")
                speak("sir, whose whatsapp chat will you like to open") 
                wh=self.takecommand().lower()
                speak("sir, please wait a second")
                pyautogui.keyDown("Ctrl")
                press("f")
                pyautogui.keyUp("Ctrl")
                speak("finding " + (wh))
                pyautogui.typewrite(wh)
                time.sleep(2)
                pyautogui.press("enter")
                speak("sir, whatsapp chat is open of " + (wh))  

            elif "WhatsApp search" in self.query: 
                speak("sir, to whom will like to search")
                pyautogui.keyDown("Ctrl")
                press("f")
                pyautogui.keyUp("Ctrl")
                pyautogui.keyDown("Ctrl")
                press("a")
                pyautogui.keyUp("Ctrl")
                se=self.takecommand().lower()
                speak("finding " + (se))
                pyautogui.typewrite(se)
                time.sleep(2)
                pyautogui.press("enter")
                speak("sir, whatsapp chat is open of " + (se)) 

            elif "type message" in self.query or "type the message" in self.query: 
                speak("ok sir")
                pyautogui.click(792,734)
                speak("sir, what message would you will like to send")
                pyautogui.keyDown("Ctrl")
                press("a")
                pyautogui.keyUp("Ctrl") 
                ty=self.takecommand().lower()
                pyautogui.typewrite(ty)
                speak("sir, your message is " + (ty))
                pyautogui.press("enter")
                speak("sir, you have successfully sended your whatsapp message")

            elif "pin the chat" in self.query or "pin chat" in self.query: 
                speak("ok sir") 
                pyautogui.keyDown("Ctrl")
                pyautogui.keyDown("Shift")
                press("p")
                pyautogui.keyUp("Shift")
                pyautogui.keyUp("Ctrl")   
                speak("sir, you have successfully pin whatsapp chat")


            elif "my profile" in self.query: 
                speak("ok sir, opening your profile")
                pyautogui.keyDown("Ctrl")
                press("p")
                pyautogui.keyUp("Ctrl")
                speak("sir, you have successfully open your profile")    

            elif "send WhatsApp message" in self.query:
                webbrowser.open("https://web.whatsapp.com/")
                speak("genrating whatsapp message, please wait a second.")
                speak("sir, to whom you would like to send message?") 
                ap = self.takecommand().lower()
                print(pyautogui.position())
                pyautogui.click(184,189)
                pyautogui.typewrite(ap)
                speak("sir, message is getting ready for "+ (ap)) 
                speak("sir, what message would like to send")
                message = self.takecommand().lower()
                pyautogui.click(163,319)
                pyautogui.typewrite(message)
                press('enter')
                speak("congratulations sir, your message as been Sent Successfully!")         

            elif "WhatsApp call" in self.query:
                npath = "C:\\Users\\HP\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
                os.startfile(npath)
                speak("ok sir, genrating whatsapp call, please wait a second.")
                speak("sir, to whom you would like to call?") 
                ap = self.takecommand().lower()
                speak("ok sir, calling to"+ (ap))
                time.sleep(3)
                print(pyautogui.position())
                pyautogui.click(250,108)
                pyautogui.typewrite(ap)
                time.sleep(3)
                pyautogui.click(223,238)
                pyautogui.click(1203,60)
                speak("congratulations sir, you have call successfully!")

            elif "video call" in self.query:
                npath = "C:\\Users\\HP\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
                os.startfile(npath)
                speak("ok sir, genrating vedio call, please wait a second.")
                speak("sir, to whom you would like to call?") 
                ap = self.takecommand().lower()
                speak("ok sir, calling to"+ (ap))
                time.sleep(3)
                print(pyautogui.position())
                pyautogui.click(250,108)
                pyautogui.typewrite(ap)
                time.sleep(3)
                pyautogui.click(223,238)
                pyautogui.click(1149,57)
                speak("congratulations sir, you have call successfully!")
                pyautogui.keyDown("win")
                pyautogui.press("up")
                pyautogui.keyUp("win")

            elif "reject call" in self.query or "reject the call" in self.query: 
                speak("ok sir, rejecting call") 
                pyautogui.click(1313,66)
                pyautogui.click(845,689)
                speak("sir, call is rejected") 

            #############  EMAIL Automation   ###############
            #################################################
            
            elif "open mail" in self.query or "open the mail" in self.query:
                speak("opening email")
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
                speak("sir, email as open successfully")          

            elif "generate email" in self.query:
                speak("ok sir, generating email, please wait a second")
                try:
                    speak("sir, please speak the subject of email")
                    sub = self.takecommand().lower()
                    speak("sir, please speak the message")
                    mess = self.takecommand().lower() 
                    speak("sir, please enter the email in terminal to whom you have to send")
                    to = input()    
                    sendEmail(to, sub, mess)
                    speak("congratulations sir, your Email as been Sent Successfully!")
                    webbrowser.open("https://mail.google.com/mail/u/0/#sent")

                except Exception as e:
                    print(e)
                    speak("sorry sir, something went wrong, i am not able to send the email")     

            elif "write email" in self.query:
                speak("ok sir, creating email")
                pyautogui.click(67,195)
                speak("sir, please enter the email in terminal to whom you have to send")
                ta = input()
                pyautogui.typewrite(ta)
                time.sleep(2)
                pyautogui.press("enter")
                speak("sir, email id  as been written successfully")  

            elif "email subject" in self.query:
                speak("ok sir, writing email subject")
                pyautogui.click(841,320)
                speak("sir, please speak the subject of email")
                subj = self.takecommand().lower()
                pyautogui.typewrite(subj)
                speak("sir, email subject as been type successfully")  

            elif "email message" in self.query:
                speak("ok sir, writing email message")
                pyautogui.click(905,396)
                speak("sir, please speak the message")
                messs = self.takecommand().lower()
                pyautogui.typewrite(messs)
                speak("sir, email message as been type successfully")  

            elif "email file" in self.query:
                speak("ok sir, attaching email file")
                pyautogui.click(957,685)
                speak("sir, please tell the name of attachment file")
                at = input()
                pyautogui.typewrite(at)
                time.sleep(2)
                pyautogui.press("enter")
                speak("sir, email file as been attached successfully")  

            elif "send email" in self.query:
                speak("ok sir, sending email file") 
                pyautogui.keyDown("Ctrl")
                pyautogui.press("enter")
                pyautogui.keyUp("Ctrl")

                time.sleep(2)
                pyautogui.press("enter")
                speak("sir, email as been send successfully")  

            elif "email search" in self.query:
                speak("ok sir, searching email")
                pyautogui.click(371,135)
                time.sleep(2)
                pyautogui.keyDown("Ctrl")
                press("a")
                pyautogui.keyUp("Ctrl")
                speak("sir, please tell the name of attachment file")
                sea = self.takecommand().lower()
                pyautogui.typewrite(sea)
                time.sleep(2)
                pyautogui.press("enter")
                speak("sir, email as been search successfully")  

            elif "email inbox" in self.query:
                speak("ok sir, opening inbox emails")
                #pyautogui.click(78,257)
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
                speak("sir, inbox email  as open successfully") 

            elif "email send" in self.query:
                speak("ok sir, opening send emails")
                #pyautogui.click(71,354)
                webbrowser.open("https://mail.google.com/mail/u/0/#sent")
                speak("sir,  send emails  as open successfully")    

            elif "email drift" in self.query:
                speak("ok sir, opening drafts emails")
                #pyautogui.click(73,383)
                webbrowser.open("https://mail.google.com/mail/u/0/#drafts")
                speak("sir,  drafts emails as open successfully")   

            elif "email all" in self.query:
                speak("ok sir, opening all emails")
                #pyautogui.click(75,420)
                webbrowser.open("https://mail.google.com/mail/u/0/#all")
                speak("sir, all emails option as open successfully")  

            elif "email spam" in self.query:
                speak("ok sir, opening spam emails")
                #pyautogui.click(75,420)
                webbrowser.open("https://mail.google.com/mail/u/0/#all")
                speak("sir, spam emails as open successfully")   

            elif "email deleted" in self.query:
                speak("ok sir, opening bin emails")
                #pyautogui.click(75,420)
                webbrowser.open("https://mail.google.com/mail/u/0/#trash")
                speak("sir, bin emails as open successfully")   

            elif "email important" in self.query:
                speak("ok sir, opening important emails")
                #pyautogui.click(75,420)
                webbrowser.open("https://mail.google.com/mail/u/0/#imp")
                speak("sir, important emails as open successfully")               

            elif "forward email" in self.query:
                speak("ok sir, forwarding email")
                pyautogui.press("End")
                time.sleep(2)
                pyautogui.click(500,590) 
                speak("sir, please enter the email in terminal to whom you have to send")
                taa = input()
                pyautogui.typewrite(taa)
                time.sleep(2)
                pyautogui.keyDown("Ctrl")
                pyautogui.press("enter")
                pyautogui.keyUp("Ctrl")
                time.sleep(2)
                pyautogui.press("enter")
                speak("sir, email is successfully forwarded to" + (taa))

            elif "reply email" in self.query:
                speak("ok sir, replying email")
                pyautogui.press("End")
                time.sleep(2)
                pyautogui.click(380,589) 
                speak("sir, please tell message for relpy")
                taa = self.takecommand().lower()
                pyautogui.typewrite(taa)
                time.sleep(2)
                pyautogui.keyDown("Ctrl")
                pyautogui.press("enter")
                pyautogui.keyUp("Ctrl")
                time.sleep(2)
                pyautogui.press("enter")
                speak("sir, you have successfully reply")
                
            #############  file manager Automation   ###############
            ########################################################    
            elif "c Drive" in self.query or "C Drive" in self.query:
                speak("ok sir, opening c drive")
                npath = "C:\\"
                os.startfile(npath)
                speak("sir, c drive as open successfully")

            elif "d Drive" in self.query or "D drive" in self.query:
                speak("ok sir, opening d drive")
                npath = "D:\\"
                os.startfile(npath)
                speak("sir, d drive as open successfully")  

            elif "e Drive" in self.query or "E drive" in self.query:
                speak("ok sir, opening e drive")
                npath = "E:\\"
                os.startfile(npath)
                speak("sir, e drive as open successfully")   

            elif "folder 1" in self.query:
                speak("ok sir, opening folder one") 
                pyautogui.press("down") 
                pyautogui.press("up") 
                pyautogui.press("enter")
                speak("sir, first folder as open successfully") 

            elif "folder 2" in self.query:
                speak("ok sir, opening folder two") 
                pyautogui.press("down") 
                pyautogui.press("enter")
                speak("sir, second folder as open successfully") 

            elif "folder 3" in self.query:
                speak("ok sir, opening folder third") 
                pyautogui.press("down" , presses=2) 
                pyautogui.press("enter")
                speak("sir, third folder as open successfully")

            elif "folder 4" in self.query:
                speak("ok sir, opening folder fourth") 
                pyautogui.press("down" , presses=3) 
                pyautogui.press("enter")
                speak("sir, fourth folder as open successfully")    

            elif "folder 5" in self.query:
                speak("ok sir, opening folder fifth") 
                pyautogui.press("down" , presses=4) 
                pyautogui.press("enter")
                speak("sir, fifth folder as open successfully")    

            elif "folder 6" in self.query:
                speak("ok sir, opening folder sixth") 
                pyautogui.press("down" , presses=5) 
                pyautogui.press("enter")
                speak("sir, sixth folder as open successfully")

            elif "folder 7" in self.query:
                speak("ok sir, opening folder seventh") 
                pyautogui.press("down" , presses=6) 
                pyautogui.press("enter")
                speak("sir, seventh folder as open successfully")

            elif "folder 8" in self.query:
                speak("ok sir, opening folder eight") 
                pyautogui.press("down" , presses=7) 
                pyautogui.press("enter")
                speak("sir, eight folder as open successfully")  

            elif "folder 9" in self.query:
                speak("ok sir, opening folder nine") 
                pyautogui.press("down" , presses=8) 
                pyautogui.press("enter")
                speak("sir, nine folder as open successfully")

            elif "folder 10" in self.query:
                speak("ok sir, opening folder tenth") 
                pyautogui.press("down" , presses=9) 
                pyautogui.press("enter")
                speak("sir, tenth folder as open successfully")          


                
                       
                   
            





            elif "on Wi-Fi" in self.query or "on the Wi-Fi" in self.query:  
                speak("ok sir, onning wifi")
                pyautogui.keyDown("win")
                press("a")
                pyautogui.keyUp("win")
                time.sleep(2)
                pyautogui.press("enter")
                pyautogui.press("esc")
                speak("sir, you have successfully on wifi")

            elif "of Wi-Fi" in self.query or "of the Wi-Fi" in self.query:  
                speak("ok sir, offing wifi")
                pyautogui.keyDown("win")
                press("a")
                pyautogui.keyUp("win")
                time.sleep(2)
                pyautogui.press("enter")
                pyautogui.press("esc")
                speak("sir, you have successfully off wifi")  

            elif "on Bluetooth" in self.query or "on the Bluetooth" in self.query:  
                speak("ok sir, onning bluetooth")
                pyautogui.keyDown("win")
                press("a")
                pyautogui.keyUp("win")
                time.sleep(2)
                pyautogui.press("right")
                time.sleep(1)
                pyautogui.press("enter")
                pyautogui.press("esc")
                speak("sir, you have successfully on bluetooth")

            elif "of Bluetooth" in self.query or "of the Bluetooth" in self.query:  
                speak("ok sir, offing bluetooth")
                pyautogui.keyDown("win")
                press("a")
                pyautogui.keyUp("win")
                time.sleep(2)
                pyautogui.press("right")
                time.sleep(1)
                pyautogui.press("enter")
                pyautogui.press("esc")
                speak("sir, you have successfully off bluetooth")  

            elif "on hotspot" in self.query or "on the hotspot" in self.query:  
                speak("ok sir, onning hotspot")
                pyautogui.keyDown("win")
                press("a")
                pyautogui.keyUp("win")
                time.sleep(2)
                pyautogui.press("left", presses=2)
                time.sleep(1)
                pyautogui.press("enter")
                pyautogui.press("esc")
                speak("sir, you have successfully on hotspot") 

            elif "of hotspot" in self.query or "of the hotspot" in self.query:  
                speak("ok sir, offing hotspot")
                pyautogui.keyDown("win")
                press("a")
                pyautogui.keyUp("win")
                time.sleep(2)
                pyautogui.press("left", presses=2)
                time.sleep(1)
                pyautogui.press("enter")
                pyautogui.press("esc")
                speak("sir, you have successfully of hotspot")               

            elif "the time" in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M")
                speak(f"sir, the time is {strTime}") 

            elif "hello" in self.query:  
                speak("Hello sir, how are you ?")

            elif "fine" in self.query:  
                speak("that's great to here, sir")  

            elif "how are you" in self.query:  
                speak("i am, perfectly fine sir and good wishes for your better future sir")      

            elif "thank you" in self.query:  
                speak("you are welcome, sir")

            
            elif "schedule my day" in self.query:
                tasks = [] #Empty list 
                speak("Do you want to clear old tasks (Plz speak YES or NO)")
                query = self.takecommand().lower()
                if "yes" in query:
                    speak("ok sir, you have cleared old tasks now you can enter new task's")
                    file = open("tasks.txt","w")
                    file.write(f"")
                    file.close()
                    while True:
                        speak("sir, you can enter your task's")
                        #no_tasks = int(input("Enter the no. of tasks :- "))
                        no_tasks = self.takecommand().lower()
                        #speak("sir you can enter your second task's")
                        #no2_tasks = self.takecommand().lower()
                        #tasks.append(input("Enter the task :- "))
                        file = open("tasks.txt","a")
                        file.write(f" {no_tasks}\n")
                        #file.write(f" {no2_tasks}\n")
                        file.close()
                        speak("sir, for continue please say next and for stop please say stop")
                        a = takecommand(self).lower()
                        if "next" in a:
                            pass
                        if "stop" in a:
                            break
                    speak("sir you have enter your task's successfully")
                elif "no" in query:
                    speak("ok sir, old tasks are not deleted but then also you can enter new task's")
                    speak("sir, you can enter your task's")
                    #no_tasks = int(input("Enter the no. of tasks :- "))
                    no_tasks = self.takecommand().lower()
                    #speak("sir you can enter your second task's")
                    #no2_tasks = self.takecommand().lower()
                    #no_tasks = int(input("Enter the no. of tasks :- "))
                    file = open("tasks.txt","a")
                    file.write(f" {no_tasks}\n")
                    #file.write(f" {no2_tasks}\n")
                    file.close()
                    while True:
                        speak("sir, for continue please say next and for stop please say stop")
                        a = takecommand(self).lower()
                        if "next" in a:
                            pass
                        if "stop" in a:
                            break
                    speak("sir you have enter your task's successfully")                   

            elif "show my schedule" in self.query:
                speak("ok sir, showing your schedule")
                file = open("tasks.txt","r")
                content = file.read()
                file.close()
                notification.notify(
                    title = "My schedule :-",
                    message = content,
                    timeout = 15
                    ) 
                print(content)
                speak(content) 
                speak("that's all sir, you have schedule")

            elif "save of" in self.query:
                tasks = [] #Empty list 
                speak("Do you want to delete old save of the day (Plz speak YES or NO)")
                query = self.takecommand().lower()
                if "yes" in query:
                    speak("ok sir, you have deleted old save of the day now you can enter new save of day")
                    file = open("save.txt","w")
                    file.write(f"")
                    file.close()
                    while True:
                        speak("sir, please tell your save of the day")
                        #no_tasks = int(input("Enter the no. of tasks :- "))
                        no_tasks = self.takecommand().lower()
                        #speak("sir you can enter your second task's")
                        #no2_tasks = self.takecommand().lower()
                        #tasks.append(input("Enter the task :- "))
                        file = open("save.txt","a")
                        file.write(f" {no_tasks}\n")
                        #file.write(f" {no2_tasks}\n")
                        file.close()
                        speak("sir, for continue please say next and for stop please say stop")
                        a = takecommand(self).lower()
                        if "next" in a:
                            pass
                        if "stop" in a:
                            break
                    speak("sir you have enter your save of the day successfully")
                elif "no" in query:
                    speak("ok sir, old save of the day are not deleted but then also you can enter new save of the day")
                    speak("sir, please tell your save of the day")
                    #no_tasks = int(input("Enter the no. of tasks :- "))
                    no_tasks = self.takecommand().lower()
                    #speak("sir you can enter your second task's")
                    #no2_tasks = self.takecommand().lower()
                    #no_tasks = int(input("Enter the no. of tasks :- "))
                    file = open("save.txt","a")
                    file.write(f" {no_tasks}\n")
                    #file.write(f" {no2_tasks}\n")
                    file.close()
                    while True:
                        speak("sir, for continue please say next and for stop please say stop")
                        a = takecommand(self).lower()
                        if "next" in a:
                            pass
                        if "stop" in a:
                            break
                    speak("sir, you have enter your save of the day successfully") 

            elif "last time" in self.query:
                speak("ok sir, calculating task's please wait a second")
                file = open("save.txt","r")
                content = file.read()
                file.close()
                notification.notify(
                    title = "My Save Of The Day :-",
                    message = content,
                    timeout = 15
                    ) 
                print(content)
                speak(content)  
                speak("that's all sir, we were doing last time")             
                
            elif "open PDF reader" in self.query:
                speak("opening pdf reader")
                npath = "C:\\Users\Public\\Desktop\\Adobe Reader XI.lnk"
                os.startfile(npath)
                speak("sir, pdf reader as open successfully")    

            elif "open CMD" in self.query: 
                speak("opening command prompt")
                #os.system("start cmd")
                npath = "C:\\WINDOWS\\system32\\cmd.exe"
                os.startfile(npath)
                speak("sir, command prompt as open successfully")
            elif "close CMD" in self.query:
                speak("ok sir, closing  command promt")
                os.system(f"taskkill /f /im cmd.exe")
                speak("sir, command prompt has been closed successfully")    

            elif "open camera" in self.query:
                speak("opening camera")
                npath = "C:\\Users\\HP\\AppData\\Local\\Camera.lnk"
                os.startfile(npath)
                speak("sir, camera as open successfully")
            elif "close camera" in self.query:
                speak("ok sir, closing  camera")
                pyautogui.keyDown("ALT")
                pyautogui.press("F4")
                pyautogui.keyUp("ALT")
                time.sleep(1)
                speak("sir, camera has been closed successfully")

            elif "take photo" in self.query or "take the photo" in self.query:
                speak("sir, taking photo, please smile.")
                pyautogui.press("enter")
                speak('sir, you have taken photo successfully') 

              

            elif "from pc" in self.query or "from the pc" in self.query:
                speak("ok sir")
                pyautogui.keyDown("win")
                press("S")
                pyautogui.keyUp("win")
                speak("sir, what would you will like to find")
                f=self.takecommand().lower()
                speak("sir, please wait a second")
                speak("finding " + (f))
                pyautogui.typewrite(f)
                time.sleep(6)
                press("enter")
                speak("sir, you have successfully finded " + (f))              
                
            
                    
                    
            
            elif "play songs"  in self.query or "play the songs"  in self.query:
                speak("playing musics")
                nn = int(datetime.datetime.now().hour)
                music_dir = "D:\\musics"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                os.startfile(os.path.join(music_dir, rd))  
       
                
            elif "IP address" in self.query:
                speak("sir, please wait a second browsing your ip address")
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")

            elif "wikipedia" in self.query:
                speak("searching wikipedia....")
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences=4)
                webbrowser.open(results)
                speak("according to wikipedia")
                speak(results) 

            elif "calculate" in self.query:
                speak("calulating results....")
                query = query.replace("calculate","")
                a=webbrowser.open(f"{query}") 
                speak("sir, here is the answer you are looking for") 

            #elif "temperature" in query: 
                #search = "temperature in kopargaon"
                #url = f"https://www.google.com/search?q={search}"     
                #r=requests.get(url) 
                #date = beautifulsoup4(r.text,"html.parser")
                
                #temp = date.find("div",class_="BNeawe").text
                #speak(f"current {search} is {temp}") 

            elif "activate search" in self.query or "activate the search" in self.query:
                speak("ok sir search mode is activated.") 
                speak("sir, what would you like to search")
                how = self.takecommand().lower()
                speak("ok sir, searching" + (how))
                max_results = 1
                how_to = search_wikihow(how,max_results)
                assert len(how_to) ==1
                how_to[0].print()
                speak(how_to[0].summary) 
                
            elif "open Facebook" in self.query:
                speak("opening facebook")
                webbrowser.open("www.facebook.com") 
                speak("sir, facebook as open successfully")   

            elif "open Instagram" in self.query:
                speak("opening instagram")
                webbrowser.open("www.instagram.com")
                speak("sir, instagram as open successfully")   

            #elif "download Instagram profile" in self.query:
                speak(" ok sir, please enter username")
                name= input()
                webbrowser.open(f"www.instagram.com/{name}")
                speak('sir here is the profile of user {name}')
                time.sleep(5)
                speak("sir would you like to download profile.")
                condition = self.takecommand().lower()
                if "yes" in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only=True)
                    speak("i am done sir")
                else:
                    pass      

            elif "open LinkedIn" in self.query:
                speak("opening linkedin")
                webbrowser.open("www.linkedin.com") 
                speak("sir, linkedin as open successfully")

            elif "open Google" in self.query:
                speak("opening google")
                speak("sir, what should i search on google")
                cm = self.takecommand().lower()
                webbrowser.open(f"{cm}") 
                speak("sir, here are the web results you are looking for.")

            elif "close Chrome" in self.query:
                speak("ok sir, closing  chrome")
                os.system(f"taskkill /f /im chrome.exe")
                speak("sir, chrome has closed successfully") 

                
            elif "open map" in self.query:
                webbrowser.open("googlemaps.com")
                speak("ok sir, opening googlemaps")
                time.sleep(5)
                print(pyautogui.position())
                pyautogui.click(372,131)
                time.sleep(2)
                speak("sir, please tell your starting location")
                bp = self.takecommand().lower()
                speak("is your starting location" + (bp))
                pyautogui.typewrite(bp)
                time.sleep(2)
                pyautogui.click(155,233)
                speak("sir, please tell destination to reach?")
                pyautogui.click(155,233)
                ap = self.takecommand().lower()
                speak("ok sir, finding" + (ap))
                pyautogui.typewrite(ap)
                time.sleep(2)
                pyautogui.click(185,299)
                pyautogui.click(467,651)
                speak("congratulations sir, you have successfully finded destination!") 

            elif "set alarm" in self.query:
                speak("sir, wait a second, setting the alarm")
                try:
                    speak("sir, tell the time")
                    ti = self.takecommand(self)
                    speak("sir, you have successfully set the alarm")
                    while True:
                        ti_ac = datetime.datetime.now()
                        now = ti_ac.strftime("%H%M")
                        if now == ti:
                            speak("time to wakeup sir")
                            music_dir = 'D:\\alarm'
                            songs = os.listdir(music_dir)
                            os.startfile(os.path.join(music_dir, songs[0]))
                            speak('sir, wakeup fast, now alarm is closed. wake up sir.')
                            condition = takecommand(self).lower()
                            if "stop" in condition:
                                speak("ok sir")
                                break     
                        elif now>ti:
                            break
                except Exception as e:
                    print(e)
                    speak("sorry sir, something went wrong, or else some informations is missing try again later")          
                    

            elif "tell a jokes" in self.query or "tell the jokes" in self.query or "tell jokes" in self.query:
                speak("ok sir")
                jokes = pyjokes.get_joke()
                print(jokes)
                speak(jokes)           

            elif "shutdown" in self.query:
                speak("ok sir, the system is to be shutdown now.")
                os.system("shutdown /s /t 5")  

            elif "restart" in self.query:
                speak("ok sir, the system is restarting now.")
                os.system("restart /r /t 5")     

            elif "tell news" in self.query or "tell the news" in self.query:
                speak("ok sir, fetching latest news please wait a second")
                #latestnews()
                api_dict = {"business" : "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=b9566ae1ff4844398a46b8fd6f2c75f0",
                "entertainment" : "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=b9566ae1ff4844398a46b8fd6f2c75f0",
                "health" : "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=b9566ae1ff4844398a46b8fd6f2c75f0",
                "science" :"https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=b9566ae1ff4844398a46b8fd6f2c75f0",
                "sports" :"https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=b9566ae1ff4844398a46b8fd6f2c75f0",
                "technology" :"https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=b9566ae1ff4844398a46b8fd6f2c75f0"}
                content = None
                url = None
                speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
                #field = input("Type field news that you want: ")
                field = self.takecommand().lower()
                for key ,value in api_dict.items():
                    if key.lower() in field.lower():
                        url = value
                        print(url)
                        print("url was found")
                        break
                    else:
                        url = True
                if url is True:
                    print("url not found")
                news = requests.get(url).text
                news = json.loads(news)
                speak("Here is the first news.")
                arts = news["articles"]
                for articles in arts :
                    article = articles["title"]
                    print(article)
                    speak(article)
                    news_url = articles["url"]
                    print(f"for more info visit: {news_url}")
                    speak("sir, for continue please say next and for stop please say stop")
                    #a = input("[press 1 to cont] and [press 2 to stop]")
                    a = self.takecommand().lower()
                    if str(a) == "next":
                        pass
                    elif str(a) == "stop":
                        break
                speak("ok sir, thats all")
                speak("thank you, for Listening news.")
                

            elif "take screenshot"  in self.query or "take a screenshot"  in self.query or "take the screenshot"  in self.query:
                speak("sir, please tell me the name for these screen short file")  
                name = self.takecommand().lower()
                speak("sir,your screenshot file name is " + (name))
                speak("ok sir, i am taking screenshot please hold a scree for few seconds")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("i am done sir, the screenshot is save in our main folder. now i am ready for next task") 

            elif "download" in self.query:    
                speak("sir, what should you like to download from google")
                cm = self.takecommand().lower()
                webbrowser.open(f"{cm}") 
                time.sleep(7)
                print(pyautogui.position())
                pyautogui.click(252,191)
                time.sleep(2)
                pyautogui.click(60,369)
                time.sleep(8)
                pyautogui.click(1227,134)
                speak("sir, please choose the image.")
                speak("sir, for selecting image please say YES.")
                while True:
                 pyautogui.press("left")
                 condition = self.takecommand()
                 if "yes" in condition:
                    pyautogui.keyDown("ctrl")
                    pyautogui.press("s")
                    pyautogui.keyUp("ctrl")
                    time.sleep(2)
                    speak("sir, what name should i give to download file")
                    d=self.takecommand().lower()
                    pyautogui.typewrite(d)
                    time.sleep(5)
                    pyautogui.press("enter")
                    time.sleep(2)
                    speak("sir image is successfully downloaded in download folder")

                 elif "stop downloading" in condition:
                    speak("ok sir, i am closing downloading")    
                    break
                 else: 
                    pass   

            #elif "read pdf" in query:
            #   speak("ok sir opening pdf reader")
            #  os.startfile("D:\\Python Project (jarvis)\\pdf\\wt.pdf")
            # book = open("D:\\Python Project (jarvis)\\pdf\\wt.pdf","rb")
                #pdfReader = PyPDF2.PdfFileReader(book)
                #pages = pdfReader.getNumPages()
                #speak(f"total number of pages in these book is {pages} ")
                #speak("sir, from which page i shall start reaing pdf: ")
                #numpage = int(takecommand().lower())
                #speak("ok sir, ")
                #page = pdfReader.getPage(numpage)
                #text = page.extractText()
                #speak(text)

            elif "check battery" in self.query or "check the battery" in self.query: 
                import psutil
                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f"sir, our system have {percentage} percent battery") 

            elif "internat speed" in self.query:  
                st = speedtest.Speedtest()              
                dl = st.download()
                up = st.upload()
                speak(f"sir we have {dl} bit per second downloading speed and {up} bit per second uploading speed")

            elif "increase the volume" in self.query or "increase volume" in self.query:
                pyautogui.press("volumeup") 
                pyautogui.press("volumeup")
                speak("sir, volume is increase by 4 percent")

            elif "decrease the volume" in self.query or "decrease volume" in self.query:
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                speak("sir, volume is decrease by 4 percent")

            elif "mute the volume" in self.query or "mute volume" in self.query:
                pyautogui.press("volumemute")

            elif "from mobile" in self.query or "from the mobile" in self.query:
                speak("ok sir")
                speak("sir, please enter the number of which you want information")
                number= (input("Enter the number : "))
                speak("sir your number is " + (number))
                speak("ok sir, generating information please wait a second")
                valid = phonenumbers.parse(number)
                B = phonenumbers.is_valid_number(valid) 
                BC = phonenumbers.is_possible_number(valid)
                
                from phonenumbers import geocoder
                pepnumber=phonenumbers.parse(number)
                location=geocoder.description_for_number(pepnumber,"en") 

                ser_pr = phonenumbers.parse(number) 
                card=carrier.name_for_number(ser_pr,'EN')

                key = "739c14989c184764b38dc6b5d09e72ae"
                geocoder = OpenCageGeocode(key)
                query= str(location)
                result = geocoder.geocode(query) 
                #print(result)

                time_zone = phonenumbers.parse(number)
                A=timezone.time_zones_for_number(time_zone) 

                lat=result[0]['geometry']['lat']
                lng=result[0]['geometry']['lng']

                #print("The validation of given number is :" , (B))
                speak("The validation of given number is :")
                speak(B)
                #print("The Possiblity of given number is :" , (BC))
                speak("The Possiblity of given number is :")
                speak(BC)
                #print("The country of given number is :" , (location))
                speak("The country of given number is :")
                speak(location)
                #print("The network of given number is :" , (card))
                speak("The network of given number is :")
                speak(card)
                #print("The timezone of  given number is :" , (A))
                speak("The timezone of  given number is :")
                speak(A)
                #print("The latitude of  given number is :" , (lat))
                speak("The latitude of  given number is :")
                speak(lat)
                #print("The longitude of  given number is :" , (lng))
                speak("The longitude of  given number is :")
                speak(lng) 
                speak("that's all sir,  i was allowed to fetch only couple of information")         

            #elif "take a break" in self.query or "take the break" in self.query or "take break" in self.query:
                #speak("ok sir, i will take break, but you can call me any time, I will be there for you.")           
                #break

            elif "take a break" in self.query or "take the break" in self.query or "take break" in self.query:
                speak("ok sir, i will take break, but you can call me any time, I will be there for you.")           
                while True:
                 wakeup = self.takecommandforwakeup()
                 if "wake up" in wakeup or "WakeUp" in wakeup:
                    wish()
                    break


            elif "goodbye" in self.query:
                speak("sir ,you have successfully executed Exit command")
                speak("thank you sir, for using me, have a good day")
                sys.exit()

            time.sleep(2)    
            speak("sir, do you have any other work")

                  

startExecution = Mainthread()
#startExecution = QThread

class Main_GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
        self.ui.pushButton_3.clicked.connect(self.close)



    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:/Users/HP/Downloads/15.gif")   
        self.ui.jarvisUi.setMovie(self.ui.movie)     
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:/Users/HP/Downloads/9.gif")   
        self.ui.label.setMovie(self.ui.movie)     
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:/Users/HP/Downloads/8.gif")   
        self.ui.label_2.setMovie(self.ui.movie)     
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:/Users/HP/Downloads/5.gif")   
        self.ui.label_3.setMovie(self.ui.movie)     
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:/Users/HP/Downloads/5.gif")   
        self.ui.label_4.setMovie(self.ui.movie)     
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:/Users/HP/Downloads/19.gif")   
        self.ui.label_5.setMovie(self.ui.movie)     
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:/Users/HP/Downloads/19.gif")   
        self.ui.label_6.setMovie(self.ui.movie)     
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:/Users/HP/OneDrive/Pictures/26.png")   
        self.ui.label_8.setMovie(self.ui.movie)     
        self.ui.movie.start()

        self.ui.movie = QtGui.QMovie("C:/Users/HP/Downloads/24.png")   
        self.ui.label_7.setMovie(self.ui.movie)     
        self.ui.movie.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()    

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString("hh:mm:ss")
        label_date = current_date.toString(Qt.ISODate)
        self.ui.label_8.setText(label_date)
        self.ui.label_7.setText(label_time) 

         
        
app = QApplication(sys.argv)
jarvis = Main_GUI()
jarvis.show()
exit(app.exec_())

