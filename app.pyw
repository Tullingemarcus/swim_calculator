import os
import tkinter as tk
from tkinter import Text, filedialog, PhotoImage

import swim_time_calculator
from swim_time_calculator import calculateTime as calc
from swim_time_calculator import addTime

root = tk.Tk()
root.title("Swim calculator")
img = PhotoImage(file="swim_calculator/stock_image.png")
root.iconphoto(False,img)

canvas = tk.Canvas(root,height=100,width=500,bg="#263d42")
canvas.pack()

frame = tk.Frame(root,width=500, height=100,bg="white")
frame.pack(fill="x")

answer = tk.Frame(root,width=500, height=250,bg="gray")
answer.pack(fill="x")

timeText = tk.IntVar()
timeText.set("pace per race")
timeText=tk.Label(frame,textvariable=timeText,height=1)
timeText.place(x=20,y=40)

hour = tk.StringVar()
hourBox = tk.Entry(frame,width=2,textvariable=hour,fg="black",bg="gray",font=16)
hourBox.place(x=20,y=10)

min = tk.StringVar()
minBox = tk.Entry(frame,width=2,textvariable=min,fg="black",bg="gray",font=16)
minBox.place(x=60,y=10)

sec = tk.StringVar()
secBox = tk.Entry(frame,width=2,textvariable=sec,fg="black",bg="gray",font=16)
secBox.place(x=100,y=10)

numText = tk.IntVar()
numText.set("number of races")
numText=tk.Label(frame,textvariable=numText,height=1)
numText.place(x=200,y=40)

num = tk.IntVar()
numBox = tk.Entry(frame,width=2,textvariable=num,fg="black",bg="gray",font=16)
numBox.place(x=200, y=10)


colon1 = tk.Label(frame,text=":",bg="white")
colon1.place(x=45,y=10)
colon2 = tk.Label(frame,text=":",bg="white")
colon2.place(x=85,y=10)

calcLabel = []
series = []
def calculator():
    global calcLabel

    serie = calc(hour.get(),min.get(),sec.get(), num.get())
    series.append(serie)
    calcLabel.append(tk.Label(answer, text=serie, padx=0.1, bg="white"))
    calcLabel[-1].pack(padx=0.1,pady=0.1)

calculate = tk.Button(root,text="calculate",padx=10, 
                    pady=5,fg="white",bg="#263d42", command=calculator)
calculate.pack()

totLabel = []
temp = "00:00:00"
def total_time():
    global temp
    global series
    global totLabel
    global calcLabel
    for i in range(0, len(series)):
        temp = addTime(series[i],temp)
    series = []
    series.append(temp)
    tot = temp
    temp = "00:00:00"
    for i in range(0, len(calcLabel)):
        calcLabel[i].destroy()
    calcLabel = []
    totLabel.append(tk.Label(answer, text=tot, padx=0.1, bg="white"))
    totLabel[-1].pack(padx=0.1,pady=0.1)

total = tk.Button(root,text="calculate total time",padx=10, 
                    pady=5,fg="white",bg="#263d42", command=total_time)
total.pack()

def clear():
    global calcLabel
    global totLabel
    global series
    series = []
    for i in range(0, len(calcLabel)):
        calcLabel[i].destroy()
    calcLabel = []
    for i in range(0, len(totLabel)):
        totLabel[i].destroy()
    
    totLabel = []
clear = tk.Button(root,text="clear",padx=10, 
                    pady=5,fg="white",bg="#263d42", command=clear)
clear.pack()

root.mainloop()
