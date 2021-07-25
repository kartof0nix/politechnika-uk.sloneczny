from suma_wektor import *


msun=1.989*10**30#kg
G=6.674*10**(-11)#N m²/kg²
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
vyearth=29788.229829307355
def fg(msun,m2,r):
    return G*msun*m2/r**2
def velocità(m1,r,a):
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

while (True):
    wek=wektor(xearth,yearth)
    vxaearth,vyaearth=sklad(vector(gravity(xearth,yearth,mearth),wek.ang+180))
    vxaearth=(vxaearth/mearth)*100000
    vyaearth=(vyaearth/mearth)*100000
    xearth=vxearth*100000
    yearth=vyearth*100000
    vyearth=vyearth+vyaearth
    vxearth=vxearth+vxaearth
