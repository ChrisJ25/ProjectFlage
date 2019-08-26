
import os
import speech_recognition as sr 
import pyttsx3
import requests
import lxml.html as lh
import pandas as pd
import pyautogui
import time
import ctypes, sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

engine = pyttsx3.init()


mic_name = 'Microsoft Sound Mapper - Input'

sample_rate = 48000
chunk_size = 1024
r = sr.Recognizer() 
mic_list = sr.Microphone.list_microphone_names()

for i, microphone_name in enumerate(mic_list): 
    if microphone_name == mic_name: 
        device_id = i 

def GeneralOrder02():

    engine.say("Sir, Confirm General Order Two?")
    clearance = input('')

    if clearance == "CONFIRM. CLEARANCE CODE: 2564":
      
        engine.say("Clearance Code Confirmed. Executing General Order Two. Goodbye Sir, its been an honor")
        data_file = 'C:\\Users\\Doctor Disco\\workspace\\ProjectFlage\\CAMO.py'
        os.remove(data_file)

def GeneralOrder01():
 
    engine.say("Sir, Confirm General Order One?")
    clearance = input('')

    if clearance == 'CONFIRM. CLEARANCE CODE:2564':

        engine.say("Clearance Code Confirmed. Executing General Order One. Good Luck Sir")

def LoopVideo(int):
        pyautogui.click(1760,660) #turns off autoplay
        time.sleep(int)
        pyautogui.click(200,630)

def SkipAds():
        
        x, y = pyautogui.locateCenterOnScreen('SkipAd.jpg')
        pyautogui.click(x,y)


def Defcon1():
    global defcon
    defcon = 1   
    engine.say("Moving to high alert! Operation: Failsafe will be ready to deploy in six hours. All units are being notified of an immient threat.")    
def Defcon2():
    global defcon
    defcon = 2

def Defcon3():
    global defcon
    defcon = 3

def Defcon4():
    global defcon
    defcon = 4

def Defcon5():
        global defcon
        defcon = 5

def Write():
        engine.say("What shall I type?")
        pyautogui.click()
        with sr.Microphone(device_index = device_id, sample_rate = sample_rate,chunk_size = chunk_size) as source: 
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source) 
                text = r.recognize_google(audio)
                pyautogui.typewrite(text)
        
        

def OpenEmail():
        pyautogui.click(630,1045)
        pyautogui.click(1885,70)
        time.sleep(1)
        pyautogui.click(1830,154)
        time.sleep(3)
        pyautogui.click(1620,200)
        engine.say("Which email would you like to open?")
        engine.runAndWait()
        with sr.Microphone(device_index = device_id, sample_rate = sample_rate,chunk_size = chunk_size) as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source) 
                text = r.recognize_google(audio)
        
        if text == "doctor":
                pyautogui.click(1600,200)
                time.sleep(6)
                pyautogui.click(1867,150)
                pyautogui.click(1500,650)
        elif text == "fallout":
                pyautogui.click(1600,200)
        elif text == "hydra":
                pyautogui.click(1600,200)
                time.sleep(6)
                pyautogui.click(1867,150)
                pyautogui.click(1500, 450)

def OpenNetflix():
        engine.say("Opening netflix, sir.")
        engine.runAndWait()
        pyautogui.click(630,1045)
        pyautogui.click(1885,70)
        time.sleep(2)
        pyautogui.click(1830,154)
        time.sleep(3)
        pyautogui.click(403,23)
        time.sleep(1)
        pyautogui.click(1200,750)
        time.sleep(3)
        pyautogui.click(1000,500)
        time.sleep(2)
        engine.say("Enjoy your netflix session, sir.")
        
        engine.runAndWait()

def OpenPowerschool():
        pyautogui.click(630,1045)
        pyautogui.click(1885,70)
        time.sleep(1)
        pyautogui.click(1830,154)
        time.sleep(3)
        usernamestr = 'Johnston503'
        passwordstr = 'NRGINCHP'



engine.say("Hello sir. What can I do for you?")
engine.runAndWait()

with sr.Microphone(device_index = device_id, sample_rate = sample_rate,chunk_size = chunk_size) as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source) 
    text = r.recognize_google(audio)
    

if text == "execute general order one":
        GeneralOrder01()

elif text == "execute general order two":
        GeneralOrder02()

elif text == "open Netflix":
        OpenNetflix()

elif text == "skip ads":
        SkipAds()

elif text == "loop video":
        engine.say("What is the video length?")
        engine.runAndWait()
        LoopVideo()

elif text == "write":
        Write()

elif text == "shutdown":
        engine.say("Affirmative, sir. Shutting down.")
        engine.runAndWait()
        exit()

elif text == "open email":
        OpenEmail()

elif text == "open grades":
        OpenPowerschool()











