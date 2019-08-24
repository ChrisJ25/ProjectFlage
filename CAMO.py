
import os
import speech_recognition as sr 
import pyttsx3

engine = pyttsx3.init()


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


def Defcon1():
    global defcon
    previousdefcon = defcon
    defcon = 1
   
    engine.say("Moving to high alert! Operation: Failsafe will be ready to deploy in six hours. All units are being notified of the immient threat. Anything I should tell them?")
    message = input('')

    engine.say("Very well sir, alerting all units.")

def Defcon2():
    global defcon
    previousdefcon = defcon
    defcon = 2

def Defcon3():
    global defcon
    previousdefcon = defcon
    defcon = 3

def Defcon4():
    global defcon
    previousdefcon = defcon
    defcon = 4

def Defcon5():
    global defcon
    previousdefcon = defcon
    defcon = 5
    


engine.say("Hello sir. What can I do for you?")
engine.runAndWait()
print('running')
mic_name = 'Microsoft Sound Mapper - Input'

sample_rate = 48000
chunk_size = 1024
r = sr.Recognizer() 
mic_list = sr.Microphone.list_microphone_names()

for i, microphone_name in enumerate(mic_list): 
    if microphone_name == mic_name: 
        device_id = i 
with sr.Microphone(device_index = device_id, sample_rate = sample_rate,chunk_size = chunk_size) as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source) 
    text = r.recognize_google(audio) 
    print ("you said: " + text) 











