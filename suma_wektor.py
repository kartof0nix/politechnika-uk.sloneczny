import math

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
    x = math.sin(math.radians(kat)) * a.len
    y = math.cos(math.radians(kat)) * a.len

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
    
    return(vector(kat, sila))

def sum_wektorowa(*argv):
    katy = []
    sily = []
    a=0
    for arg in argv:
        if(a%2 == 0):
            katy.append(arg)
        else:
            sily.append(arg)
        a+=1
    ixy = [0] * len(katy)
    yg = [0] * len(katy)
    for i in range(len(katy)):
        ixy[i], yg[i] = sklad(katy[i], sily[i])
        ixy[i], yg[i] = round(ixy[i], 10), round(yg[i], 10)
    print(ixy, yg)





