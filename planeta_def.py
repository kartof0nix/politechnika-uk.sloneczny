from suma_wektor import *
from turtle import *



global planety
planety = []



class planeta():

    msun=1.989*10**30#kg
    G=6.674*10**(-11)#N m^2/kg^2
    #mearth=5.972*10**24#kg
    mearth=5.972*10**24#kg
    aearth=149.6*10**9#m
    #bearth=149579137573.31802
    #cearth=2498320000.0000753
    #eearth=0.0167

    #ys=0
    #xs=0

    xearth=149.6*10**9
    yearth=0
    vxearth=0
    vyearth=29788.229829307355 #m/s
    #vyearth=6788.229829307355

    def __init__(self, name, color, m_planet = 5.972*10**24, x_cor_planet = 149.6*10**9, y_cor_earth = 0, V_xearth = 0, V_yearth=29788.229829307355) -> None:
        planety.append(self)
        self.num = len(planety)-1
        self.color = color
        self.name = name
        self.mearth = m_planet
        self.xearth = x_cor_planet
        self.yearth = y_cor_earth
        self.vxearth = V_xearth
        self.vyearth = V_yearth
        self.xpop = x_cor_planet
        self.ypop = y_cor_earth
        pass

    def fg(self, msun,m2,r):
        #if(r==0):
            #return 0
        return self.G*msun*m2/r**2
    def velocita(self, m1,r,a):
        return (self.G*m1*((2/r)-(1/a)))**(1/2)
    def b(self, e,a):
        return a*(1-e**2)**(1/2)
    def c (self, a,b):
        return ((a**2)-(b**2))**(1/2)
    def T (self, a,m1):
        return (4*(3.14**2)*a**3/(self.G*m1))**(1/2)


    def gravity(self, x,y,m1, m2):
        return self.fg(m1, m2,((x**2)+(y**2))**(0.5))

    def do_tick(self, time_passed):
        #print("X: " + str(self.xearth))
        #print("Y: " + str(self.yearth))
        self.xpop = self.xearth
        self.ypop = self.yearth

        sily = []
        for i in range(len(planety)):
            if(self == planety[i]):
                continue
            if(i < self.num): #If already processed
                x, y = self.xearth - planety[i].xpop, self.yearth - planety[i].ypop
                wek=wektor(x,y)
                sily.append(vector(self.gravity(x,y, planety[i].mearth, self.mearth),wek.ang+180))
            if(i > self.num): #If already processed
                x, y = self.xearth - planety[i].xearth, self.yearth - planety[i].yearth
                wek=wektor(x,y)
                sily.append(vector(self.gravity(x, y, planety[i].mearth, self.mearth),wek.ang+180))

        vxaearth, vyaearth=sklad(sum_wektorowa(sily))
        #print("Przysp. : " +str(vxaearth) + ", " + str(vyaearth))
        #vxaearth,vyaearth = sklad()
        vxaearth=(vxaearth/self.mearth) * time_passed
        vyaearth=(vyaearth/self.mearth) * time_passed
        #print("Pred. z a: " +str(vxaearth) + ", " + str(vyaearth))
        #print("Pred. dodaw: " +str(self.vxearth) + ", " + str(self.vyearth))
        self.vyearth=self.vyearth+vyaearth
        self.vxearth=self.vxearth+vxaearth

        self.xearth+=self.vxearth * time_passed
        self.yearth+=self.vyearth * time_passed

        return(self.xearth, self.yearth)