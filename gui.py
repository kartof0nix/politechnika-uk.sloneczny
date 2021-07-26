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
import tkinter as tk
class obsluga():
    def __init__(self):
        self.exists = True

        self.main_loop_int = 0.01
        self.paused = True
        self.root = tk.Tk()
        self.text = tk.StringVar()
        self.text.set("Test")
        #self.label = tk.Label(self.root, textvariable=self.text)

        self.menu = tk.Frame(self.root, )
        self.p_button = tk.Button(self.menu, text = "Pause")
        self.p_button ["command"] = self.pause
        self.p_button.pack(side="left", padx=10, pady=5)
        self.stop_b = tk.Button(self.menu, text="Exit", command=self.exit)
        self.stop_b.pack(side="right", padx=10, pady=5)
        self.menu.pack()
        #self.label.pack()
        #self.root.mainloop()
        self.root.update()
    def pause(self):
        self.paused = not self.paused
        if(self.paused):  
            self.p_button[ "text" ] = "Unpause"
        else:
            self.p_button[ "text" ] = "Pause" 
    def exit(self):
        self.root.destroy()
        self.exists = False