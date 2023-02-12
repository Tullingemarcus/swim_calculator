import os
import tkinter as tk
from tkinter import Text, filedialog

def calculateTime(hour,min,sec, num):
    if(hour == ""):
        hour = "00"
    if(min == ""):
        min = "00"
    if(sec == ""):
        sec = "00"

    sec = num * int(sec)
    min = num * int(min)
    hour = num * int(hour)

    secTemp = int(sec / 60)
    min = min + secTemp
    minTemp = int(min / 60)
    hour = hour + minTemp

    sec = sec % 60
    min = min % 60
    if sec < 10:
        sec = "0" + str(sec)
    if min < 10:
        min = "0" + str(min)
    if hour < 10:
        hour = "0" + str(hour)
    time = str(hour) + ":" + str(min) + ":" + str(sec)
    return time

    











