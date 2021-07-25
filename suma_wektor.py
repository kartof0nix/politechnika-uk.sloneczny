import math
def sklad(kat, sila):
    ile = (kat//90)%4
    kat = kat%90
    x = math.sin(math.radians(kat)) * sila
    y = math.cos(math.radians(kat)) * sila

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
    kat = kat + ile*90
    return(kat, sila)



