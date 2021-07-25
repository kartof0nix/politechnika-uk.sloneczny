import turtle
from suma_wektor import *
from turtle import *
import time

turtle.dot(20)
turtle.penup()
turtle.speed(0)

CONS = 1000000000
tick = 60400

msun=1.989*10**30#kg
G=6.674*10**(-11)#N m^2/kg^2
mearth=5.972*10**24#kg
aearth=149.6*10**9#m
bearth=149579137573.31802
cearth=2498320000.0000753
eearth=0.0167
ys=0
xs=0
xearth=149.6*10**9
yearth=0
vxearth=0
#vyearth=29788.229829307355 #m/s
vyearth=9788.229829307355


turtle.goto(xearth/CONS, yearth/CONS)
turtle.pendown()

def fg(msun,m2,r):
    return G*msun*m2/r**2
def velocita(m1,r,a):
    return (G*m1*((2/r)-(1/a)))**(1/2)
def b(e,a):
    return a*(1-e**2)**(1/2)
def c (a,b):
    return ((a**2)-(b**2))**(1/2)
def T (a,m1):
    return (4*(3.14**2)*a**3/(G*m1))**(1/2)


def vy(x,y):
    return

def gravity(x,y,m2):
    return fg(msun,m2,((x**2)+(y**2))**(0.5))

print("lol")
input("test")
time.sleep(1)

while (True):
    #print("X: " + str(xearth))
    #print("Y: " + str(yearth))
    wek=wektor(xearth,yearth)
    #print(wek.ang)
    vxaearth,vyaearth=sklad(vector(gravity(xearth,yearth,mearth),wek.ang+180))
    #print("Przysp. : " +str(vxaearth) + ", " + str(vyaearth))
    vxaearth=(vxaearth/mearth) * tick
    vyaearth=(vyaearth/mearth) * tick
    #print("Pred. z a: " +str(vxaearth) + ", " + str(vyaearth))

    #print("Pred. dodaw: " +str(vxearth) + ", " + str(vyearth))
    
    vyearth=vyearth+vyaearth
    vxearth=vxearth+vxaearth
    xearth+=vxearth * tick
    yearth+=vyearth * tick
    
    turtle.goto(xearth/CONS, yearth/CONS)
    #print("X: " + str(xearth))
    #print("Y: " + str(yearth))
    #print()
    #time.sleep(0.001)
    
