import math
import datetime 
class vector:
    len = 0
    ang=0
    def __init__(self, len, ang) -> None:
        self.len = len
        self.ang = ang

def sklad(a):
    a.ang = (-a.ang) + 360
    ile = (a.ang//90 + 1)%4
    
    kat = a.ang%90
    x = round(math.sin(math.radians(kat)) * a.len, 8)
    y = round(math.cos(math.radians(kat)) * a.len, 8)

    if(ile == 0):
        return(x, y)
    elif(ile == 1):
        return(y, -x)
    elif(ile == 2):
        return(-x, -y)
    elif(ile == 3):
        return(-y, x)

def wektor(x, y):
    ile = 0
    if(x >= 0 and y>=0):
        ile=0
    if(x >= 0 and y<0):
        ile=1
        x , y= -y, x
    if(x < 0 and y<0):
        ile=2
        x, y = -x, -y
    if(x < 0 and y>0):
        ile=3
        x , y= y, -x

    sila = math.sqrt(x**2 + y**2)
    kat = math.degrees(math.asin(x/sila))
    kat = kat + (ile-1)*90
    kat = -kat
    if(kat<0):
        kat+=360
    
    return(vector(round(kat, 8), round(sila, 8)))

def sum_wektorowa(*argv):
    ixy = [0] * len(argv)
    yg = [0] * len(argv)
    i=0
    for vec in argv:
        ixy[i], yg[i] = sklad(vec)
        ixy[i], yg[i] = ixy[i], yg[i]
        i+=1

    sr_x = 0
    sr_y = 0
    for i in range(len(ixy)):
        sr_x += ixy[i]
        sr_y += yg[i]
    #sr_x/=len(ixy)
    #sr_y/=len(yg)
    return(wektor(sr_x, sr_y))
#a = sum_wektorowa(vector(2, 0), vector(4.47213595, 90 -  26.56505117707799 ), vector(5, 323.13010235415595), vector(1, 270))
#print(a.ang)
#print(a.len)





