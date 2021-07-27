import tkinter as tk

import turtle
import time

from suma_wektor import *
from planeta_def import *
from gui import *


CONS = 7000000000
tick = 90400

###  ------- PLANETY
#global planety -> zdefiniowane w innym pliku, zawiera wszystkie planety

ile_pl = int(input("Ile obiektów w ukladzie?"))

if(input("Czy wypelnic Słońce i pierwsze 8 (lub ile można) planet z Ukł Słonecznego? (t/n)") == 't'):
    ile_pl +=1
    planety.append(planeta("Slonce", "#a3a133", 0.2, 1.989*10**30, 0, 0, 0, 0))
    planety.append(planeta("", "white", 0.0001, 1000, 0, 0, 0, 0))
    planety.append(planeta("Merkury", "#bf682a", 0.02, 3.285*10**23, 6.982*10**10, 0, 0, 38860 ))
    planety.append(planeta("Wenus", "#ebc06a", 0.048, 4.8675*10**24, 1.0894 * 10**11, 0, 0, 34790 ))
    #ziemia
    planety.append(planeta( "Ziemia", "lime", 0.05, 5.9726*10**24, 152097701000, 0, 0, 29291.229829307355))
    #Mars
    planety.append(planeta( "Mars", "#d64322", 0.04, 6.4185 * 10**23, 24922873 * 10**4, 0, 0, 21972))
    #Jowisz 
    planety.append(planeta( "Jowisz", "#f5ce82", 0.11, 1.898*10**27, 816081455 * 10**3, 0, 0, 12446))
    #Saturn
    planety.append(planeta( "Saturn", "#de1dae", 0.075, 5.6834*10**26, 15155*10**8, 0, 0, 9090))
    #Uran
    planety.append(planeta( "Uran", "#78a2ad", 0.065, 86.813*10**24, 3003.62 * 10**9, 0, 0, 6490))
    #Neptun
    planety.append(planeta( "Neptun", "#3e79de", 0.064, 1.0243*10**26, 45368743.25 *10**5, 0, 0, 5385))
    planety = planety[0:min(ile_pl, len(planety))]

while(len(planety) < ile_pl):
    print("Wprowadzanie planety nr. " + str(len(planety)) + ":")
    n = input("--->Nazwa :" )
    c = input("--->Kolor (HEX/red, blue, itp.) :")
    size = float(input("--->Rozmiar na reprezentacji (Słońce ma 0.2) :"))
    m = float(input("--->Masa planety :"))
    x = float(input("-->Max. odleglosc od slonca(start) :"))
    vy = float(input("--->Minimalna predkosc(start) :"))
    
    planety.append(planeta(n, c, size, m, x, vy))

    # ziemia                   size ,  mass      ,   x,          y, vx,   vy
    #planeta( "Ziemia", "blue", 0.5,  5.972*10**24, 149.6*10**9, 0, 0, 29788.229829307355)
    #Słońce
    
i = input("Edytować obiekty (nr. obiektyu / nie)? >")
while(i!='nie'):
    i=int(i)
    print("Edytowanie planety nr. " + str(i))
    planety[i].name = input(planety[i].name + "--->Nazwa :" )
    planety[i].color = input(planety[i].color + "--->Kolor (HEX/red, blue, itp.) :")
    planety[i].v_size = float(input(str(planety[i].v_size) + "--->Rozmiar na reprezentacji (Słońce ma 0.2) :"))
    planety[i].mearth = float(  input(str(planety[i].mearth)+"--->Masa planety :"))
    planety[i].xearth = float(input(str(planety[i].xearth) + "-->Max. odleglosc od slonca(start) :"))
    planety[i].vyearth = float(input(str(planety[i].vyearth) + "--->Minimalna predkosc(start) :"))
    i = input("Edytować obiekty (nr. obiektyu / nie)? >")


nazwy={
    "Ziemia":0,
    "Slonce":1
}

####   -----GUI

   
        #self.root.update()
app=obsluga()

#---- insert planets to view
  
#def __init__(self,root):
total_columns = 5   
#turtle.bgcolor('black')
app.table = tk.Frame(app.root)
    # code for creating table
for i in range(len(planety)+1):
    if(i==0):
        e = tk.Entry(app.table, width=20, bg='gray', font=('Arial',10, 'bold'))
        e.grid(row=i, column=0)
        e.insert(tk.END, "")

        e = tk.Entry(app.table, width=20, fg='black', font=('Arial',10, 'bold'))
        e.grid(row=i, column=1)
        e.insert(tk.END, "X cor [km]")

        e = tk.Entry(app.table, width=20, fg='black', font=('Arial',10, 'bold'))
        e.grid(row=i, column=2)
        e.insert(tk.END, "Y cor [km]")

        e = tk.Entry(app.table, width=20, fg='black', font=('Arial',10, 'bold'))
        e.grid(row=i, column=3)
        e.insert(tk.END, "V_x [km/s]")

        e = tk.Entry(app.table, width=20, fg='black', font=('Arial',10, 'bold'))
        e.grid(row=i, column=4)
        e.insert(tk.END, "V_y [km/s]")
        continue

    for j in range(total_columns):
        
        if(j==0):        
            e = tk.Entry(app.table, width=10, fg=planety[(i-1)].color, font=('Arial',10,'bold'))   
        else:
            e = tk.Entry(app.table, width=20, fg='black', font=('Arial',10,)) 
        e.grid(row=i, column=j)
        e.insert(tk.END, "aaa")


app.table.pack()
def refresh_table(planet):
    nr= planet
    st = total_columns*(nr + 1) + 1




    app.table.children['!entry' + str(st)].delete(0, tk.END)
    app.table.children['!entry' + str(st)].insert(tk.END, planety[nr].name)
    #app.table.children['!entry' + int(st)] ['text'] = planety[nr].name
    st+=1
    app.table.children['!entry' + str(st)].delete(0, tk.END)
    app.table.children['!entry' + str(st)].insert(tk.END, round(planety[nr].xearth / 1000, 1))

    st+=1

    app.table.children['!entry' + str(st)].delete(0, tk.END)
    app.table.children['!entry' + str(st)].insert(tk.END, round(planety[nr].yearth / 1000, 1))

    st+=1
    app.table.children['!entry' + str(st)].delete(0, tk.END)
    app.table.children['!entry' + str(st)].insert(tk.END, round(planety[nr].vxearth, 1))

    st+=1
    app.table.children['!entry' + str(st)].delete(0, tk.END)
    app.table.children['!entry' + str(st)].insert(tk.END, round(planety[nr].vyearth, 1))
    app.root.update()

    
refresh_table(0)
refresh_table(1)

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
        p_turtles[i].fd(1)
        p_turtles[i].turtlesize(planety[i].v_size, planety[i].v_size)

pop = time.time()
init_turtles()
while (app.exists):
    if(not app.paused):
        for i in range(len(planety)):
            x, y = planety[i].do_tick(tick)
        if(time.time() - pop > 0.008 ):
            for i in range(len(planety)):
                p_turtles[i].goto(planety[i].xearth/CONS, planety[i].yearth/CONS)
                refresh_table(i)
            pop = time.time()
    if(app.exists):
        app.root.update()
    #print(wek.ang)

    
    #print("X: " + str(xearth))
    #print("Y: " + str(yearth))


    #print()
    #time.sleep(0.01)
