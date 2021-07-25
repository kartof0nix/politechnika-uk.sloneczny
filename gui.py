"""
import matplotlib.pyplot as plt
import numpy as nm

x = nm.arange(-100000, 100000, 10)

def f(x):
    x**2

y=f(x)
plt.plot(x, y)
plt.show()



import tkinter as tk

class obsluga():
    def __init__(self):
        self.paused = False
        self.root = tk.Tk()
        self.text = tk.StringVar()
        self.text.set("Test")
        #self.label = tk.Label(self.root, textvariable=self.text)

        self.p_button = tk.Button(self.root,
                                textvariable=self.text,
                                command=self.pause)
        self.p_button.pack()
        #self.label.pack()
        self.root.mainloop()

    def pause(self):
        self.paused = not self.paused
        if(self.paused):
            self.text.set("Pause")   
        else:
            self.text.set("Unpause")     

#a = obsluga()

class obsluga():
    paused = True   
    pauza = tk.Button()
    def __init__(self) -> None:
        self.win = tk.Tk()
        self.win.title("Symulator układu słonecznego - Menadżer symulacji")
        greeteing = tk.Label(self.win, text="Hello there")
        greeteing.pack()
        self.text = tk.StringVar(self.win, "Pauzuj")
        self.pauza = tk.Button(self.win, textvariable=self.text, command=self.pauzuj())
        self.pauza.pack()
        self.win.mainloop()
        self.paused = False
        return 

    def pauzuj(self):
        self.paused = not self.paused
        if(self.paused):
            self.text.set("Odpauzuj")
        if(not self.paused):
            self.text.set("Zapauzuj")
    """
from tkinter import *

ROOT = Tk()
LABEL = Label(ROOT, text="Hello, world!")
LABEL.pack()
LOOP_ACTIVE = True
while LOOP_ACTIVE:
    ROOT.update()
    USER_INPUT = input("Give me your command! Just type \"exit\" to close: ")
    if USER_INPUT == "exit":
        ROOT.quit()
        LOOP_ACTIVE = False
    else:
        LABEL = Label(ROOT, text=USER_INPUT)
        LABEL.pack()