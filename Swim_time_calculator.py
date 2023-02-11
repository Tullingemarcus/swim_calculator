import os
import tkinter as tk
from tkinter import Text, filedialog

def calculateTime(hour,min,sec, num):
    if(hour.get() == ""):
        hour = "00"
    else:
        hour = hour.get()
    if(min.get() == ""):
        min = "00"
    else:
        min = min.get()
    if(sec.get() == ""):
        sec = "00"
    else:
        sec = sec.get()
    pace = min + ":" + sec
    time = 0
    min = 0
    sec = 0
    
    paceString = ""
    for letter in pace:
        if letter in ":":
            min = num * int(paceString)
            paceString = ""
        else:
            paceString += letter
    sec = num * int(paceString)
    newsec = int(sec / 60)
    min = min + newsec
    if min >= 60:
        newmin = min % 60
        if newmin <= 10:
            newmin = "0" + str(newmin)
        min = str(int(min/60)) + ":" + str(newmin)
    time = str(min) + ":" + str(sec % 60) 
    return time

    











