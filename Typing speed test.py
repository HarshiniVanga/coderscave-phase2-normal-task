# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 12:28:35 2023

@author: Harshini Vanga
"""

#import tkinter
from tkinter import *
from timeit import default_timer as timer
import random
window = Tk()
window.geometry("550x300")
x = 0
def test():
    global x
    if x == 0:
        window.destroy()
        x = x+1
    def check_result():
        if entry.get() == words[word]:
            end = timer()
            print(end-start)
        else:
            print("Invalid = Error")
 
    words = ['Harshini','Anmisha','Vyshnavi','Keerthana','Alekya','Vamshi']
 
    word = random.randint(0, (len(words)-1))
    start = timer()
    windows = Tk()
    windows.geometry("550x300")
    x2 = Label(windows, text=words[word], font="times 20")
    x2.place(x=250, y=20)
    x3 = Label(windows, text="Type the word", font="times 20")
    x3.place(x=20, y=60)
    entry = Entry(windows)
    entry.place(x=260, y=65)
    b2 = Button(windows, text="check",
                command=check_result, width=10, bg='light blue')
    b2.place(x=160, y=120)
 
    b3 = Button(windows, text="type again",
                command=test, width=10, bg='light blue')
    b3.place(x=260, y=120)
    windows.mainloop()
x1 = Label(window, text="Start the test...!!!", font="times 20")
x1.place(x=10, y=50)
b1 = Button(window, text="READY", command=test, width=10, bg='light blue')
b1.place(x=160, y=120)
window.mainloop()
