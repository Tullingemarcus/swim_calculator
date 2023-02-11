import os
import tkinter as tk
from tkinter import Text, filedialog

import Swim_time_calculator
from Swim_time_calculator import calculateTime as calc

root = tk.Tk()

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


series = []
def calculator():
    time = min.get() + ":" + sec.get()
    print(time)
    serie = calc(time, num.get())
    series.append(serie)
    label = tk.Label(answer, text=serie, padx=0.1, bg="white")
    label.pack(padx=0.1,pady=0.1)

calculate = tk.Button(root,text="calculate",padx=10, 
                    pady=5,fg="white",bg="#263d42", command=calculator)
calculate.pack()

root.mainloop()
