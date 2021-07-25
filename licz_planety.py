import tkinter as tk
import turtle
from typing import Text
from suma_wektor import *
from turtle import *
import time
from planeta_def import *
#from gui import *


CONS = 1000000000
tick = 60400

###  ------- PLANETY
#global planety -> zdefiniowane w innym pliku, zawiera wszystkie planety

# ziemia
#planeta( "Ziemia", "blue", 5.972*10**24, 149.6*10**9, 0, 0, 29788.229829307355)
planeta( "Ziemia", "blue", 1.989*10**30, 149.6*10**9, 0, 0, 14788.229829307355)
#Słońce
planeta("Slonce", "#a3a133", 1.989*10**30, 0, 0, 0, -14788.229829307355)
print(planety)

nazwy={
    "Ziemia":0,
    "Slonce":1
}

####   -----GUI

class obsluga():
    def __init__(self):
        self.main_loop_int = 0.01
        self.paused = False
        self.root = tk.Tk()
        self.text = tk.StringVar()
        self.text.set("Test")
        #self.label = tk.Label(self.root, textvariable=self.text)

        self.p_button = tk.Button(self.root, text = "Pause")
        self.p_button ["command"] = self.pause
        self.p_button.pack()
        #self.label.pack()
        #self.root.mainloop()
        self.root.update()

    def pause(self):
        self.paused = not self.paused
        if(self.paused):  
            self.p_button[ "text" ] = "Unpause"
        else:
            self.p_button[ "text" ] = "Pause"    
        #self.root.update()
app=obsluga()

###   ----Initialize turtles
p_turtles = []
def init_turtles():
    for i in range(len(planety)):
        p_turtles.append(turtle.Turtle())
        p_turtles[i].speed(0)
        p_turtles[i].color(planety[i].color)
        p_turtles[i].shape("circle")
        p_turtles[i].penup()
        p_turtles[i].goto(planety[i].xearth, planety[i].yearth)
        p_turtles[i].pendown()

init_turtles()
while (True):
    if(not app.paused):
        for i in range(len(planety)):
            x, y = planety[i].do_tick(tick)
            p_turtles[i].goto(x/CONS, y/CONS)


    app.root.update()
    #print(wek.ang)

    
    #print("X: " + str(xearth))
    #print("Y: " + str(yearth))


    #print()
    time.sleep(0.01)
