from cgitb import text
from operator import length_hint
from re import A
from time import strftime
import tkinter
from tkinter import CENTER, RIGHT, messagebox
from tkinter import Label
from tkinter import Button
from tkinter.font import BOLD
from tkinter import messagebox
import datetime
from datetime import date
from datetime import datetime
import time
from time import sleep
import sys
import threading 
import ctypes
from turtle import right
from unittest import skip



#CREATE WINDOW
win = tkinter.Tk()
win.geometry('1000x800')
win.title("Reminder and To-Do List")

#TIME AND DATE IS HANDLED
today = date.today()
today_date = tkinter.Label(win, text=today.strftime("%B %d, %Y"), font= ('Arial 25 bold'))

#ADD ITEM WIDGETS ARE CREATED 
event = tkinter.StringVar()
addEventLabel =  tkinter.Label(win, text =  "Add Event: ", font = ('Arial 20'))
addEventEntry = tkinter.Entry(win, textvariable=event,font=('Arial 15'))

eventTime = tkinter.StringVar()
addTimeLabel = tkinter.Label(win, text = "Reminder Time: ", font = ('Arial 20'))
addTimeEntry = tkinter.Entry(win, textvariable=eventTime,font=('Arial 15'))

eventDate = tkinter.StringVar()
eventDateLabel = tkinter.Label(win, text = "Reminder Date: ", font=('Arial 20'))
eventDateEntry = tkinter.Entry(win, textvariable=eventDate, font=('Arial 15'))

#TO DO LIST HEADER CREATED
todoLabel = tkinter.Label(win, text = "To-Do List:", font=('Arial 20 underline'))
todoLabel.place(relx=0.2, rely=0.15, anchor=CENTER)

#DICTIONARY WITH ALL EVENT
to_do = {}

#ALL EVENTS ARE ADDED TO DICTIONARY THEN DISPLAYED 
def entry():
    holder = []
    holder.append(event.get())

    if len(eventTime.get()) > 0:
        holder.append(eventTime.get())

    if len(eventDate.get()) > 0:
        holder.append(eventDate.get())


    to_do[event.get()] = holder
    addEventEntry.delete(first=0, last=len(event.get()))
    addTimeEntry.delete(first = 0, last = len(eventTime.get()))
    eventDateEntry.delete(first = 0, last = len(eventDateEntry.get()))


    counter = 0.18
    for i in to_do:
        counter += 0.06
        curr = to_do[i]
        if len(curr) == 1:
            tkinter.Label(win, text = "- " + str(curr[0]) + "\n", font = ('arial 15'), wraplength=300).place(relx = 0.2, rely = counter, anchor= CENTER)
        if len(curr) == 2:
            if curr[1] == None:
                skip
            else:
                tkinter.Label(win, text = "- " + str(curr[0]) + " at " + str(curr[1]) + "\n", font = ('arial 15'), wraplength=300).place(relx = 0.2, rely = counter, anchor= CENTER)
        if len(curr) == 3:
            if curr[1] == None:
                skip
            else:
                tkinter.Label(win, text = "- " + str(curr[0]) + " at " + str(curr[1]) + " on " + str(curr[2]) + "\n", font = ('arial 15'), wraplength=300).place(relx = 0.2, rely = counter, anchor= CENTER)


def updatingTime():
    while True:
        global currentTime
        currentTime = datetime.now().time()
        currentTime = strftime("%H:%M")
        today_time = tkinter.Label(win, text = currentTime, font = ('Arial 20'))
        today_time.place(relx = 0.5, rely=0.1, anchor=CENTER)

        values = list(to_do.values())
        for i in values:
            if len(i) == 2:
                if i[1] == currentTime:
                    ctypes.windll.user32.MessageBoxW(0, str(i[0]) , "Reminder", 1)
                    i[1] = None
                    break
            if len(i) == 3:
                if i[1] == currentTime:
                    if i[2] == today.strftime("%B %d, %Y"):
                        ctypes.windll.user32.MessageBoxW(0, str(i[0]) , "Reminder", 1)
                        i[1] = None
                        break
                
                    
#use threading to run the clock in the background and check if the time has been reached for any events 
clockTime = threading.Thread(target = updatingTime)
clockTime.start()


#DONE BUTTON FOR ADDING EVENT
addButton = tkinter.Button(win, text =  "Add Event", command = entry, font=('arial 15'))


#THIS IS WHERE MOST ITEMS ARE PLACED ON THE WINDOW
today_date.place(relx = 0.5, rely=0.05, anchor=CENTER)


addButton.place(relx = 0.8, rely =0.5, anchor=CENTER)


addEventLabel.place(relx = 0.65, rely=0.2, anchor=CENTER)
addEventEntry.place(relx = 0.85, rely=0.2, anchor=CENTER)

addTimeLabel.place(relx = 0.62, rely = 0.3, anchor=CENTER)
addTimeEntry.place(relx = 0.85, rely = 0.3, anchor=CENTER)

eventDateLabel.place(relx = 0.62, rely = 0.4, anchor=CENTER)
eventDateEntry.place(relx = 0.85, rely = 0.4, anchor=CENTER)


win.mainloop()


