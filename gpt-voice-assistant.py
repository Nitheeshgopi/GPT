import os
import openai
import pyttsx3
import numpy as np
import random as rn
import speech_recognition as sr
from datetime import *
import webbrowser as wb


engine=pyttsx3.init()
engine.setProperty("rate",120)
r=sr.Recognizer()
now=datetime.now()

wish=["Hello this is GPT chatbot.. How can I help you today","Hei there.. How can I help you?",]

while True:
    with sr.Microphone() as source:
     r.adjust_for_ambient_noise(source,duration=0.4)
     print("Speak After a Sec.!!")
     engine.say(rn.choice(wish))
     engine.runAndWait()
     adio=r.listen(source)
     txt=r.recognize_google(adio)
     try:
       openai.api_key = "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"
       response = openai.Completion.create(
          engine = "text-davinci-003",   #text-ada-001    text-davinci-003    
          prompt = txt,
          temperature = 0.6,
          max_tokens = 250
        )
       answer=response.choices[0].text
       engine.say(answer)
       engine.runAndWait()

     except:
         engine.say("sorry i did not get you..")
         engine.runAndWait()
    
