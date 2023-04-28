#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install pyaudio')
get_ipython().system('pip install gTTS')
get_ipython().system('pip install pydub')
get_ipython().system('pip install SpeechRecognition')
get_ipython().system('pip install playsound')


# In[ ]:


import speech_recognition as sr
import os
from playsound import playsound
from gtts import gTTS
import pyaudio
from pydub import AudioSegment
from pydub.playback import play


# In[ ]:


def speak(text):
    tts=gTTS(text=text,lang="en")
    tts.save("speech.mp3")
    playsound("speech.mp3")
    os.remove("speech.mp3")
def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        
        return text
    except:
        speak("Sorry, I didn't understand you. Can you please repeat that?")
        return listen()
def book_room():
    speak("Welcome to our hotel! what is your name?")
    name=listen()
    
    speak(f"Nice to meet you{name}.")
    speak("What's your phone number?")
    phone_number = listen()
    
    speak("What's your address?")
    address = listen()
    
    speak("What's your age?")
    age = listen()
    
    
    speak("We are accepting only licence and Adhaar!as a ID proof so What type of ID do you have?")
    id_proof = listen()

    speak("we have AC and Non AC rooms What type of room would you like to book?")
    room_type = listen()
    
    speak("When do you plan to arrive?")
    arrival_date = listen()
    
    speak("When do you plan to leave?")
    departure_date = listen()
    type_room="AC"
    type_room1="Non Ac"
    
    if not age>=20 and id_proof and room_type==type_room or room_type==type_room1  and  arrival_date and   departure_date and  phone_number:
        speak("Sorry you are not eligible to book rooms")
        
        return
    speak("Great! Here are your booking details:")
    speak(f"Name: {name}")
    
    speak(f"Your age is: {name}")
    speak(f"Phone Number: {phone_number}")
    speak(f"Address: {address}")
    speak(f"ID Proof: {id_proof}")
    speak(f"Room Type: {room_type}")
    speak(f"Arrival Date: {arrival_date}")
    speak(f"Departure Date: {departure_date}")
    speak("Thank you for choosing our hotel!")
          
book_room()


# In[ ]:




