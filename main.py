#Kinshasa, 07/08/2021
#Chadrack KANZA
#Archi-Tech 2021

import pyttsx3
engine = pyttsx3.init()

"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 125)     # setting up new voice rate

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

names = ['chadrack Kanza','John','Peter', 'Sarah', 'Thomas','Anderson', 'Dorcas']
def reader_name(namesList):
    for name in namesList:
        engine.say(name)

engine.say("These persons can come")
reader_name(names)
engine.runAndWait()
engine.stop()

