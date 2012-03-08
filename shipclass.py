#Copyright Jonathan Hennessy-Doyle 2012
#Licensed under the GPL v2
#Email jonathanhennessydoylety@gmail.com
class ship(object):
    
    def __init__(self, stype):
        if stype == "SS" :
            self.lenShip = 3
        elif stype == "CR":
            self.lenShip = 3
        elif stype == "BS":
            self.lenShip = 4
        elif stype == "CA":
            self.lenShip = 5
        elif stype == "DD":
            self.lenShip = 2
        else:
            pass
        self.currentDamage = 0
        self.type = stype
        self.wasSunk = False
        self.shipCords = []
    
    def place(self, teamShipCords): #TODO VERY wasteful and inefficient, replace ASAP
        from random import randint
        self.angle = randint(0,1)
        posx = randint(0,9)
        posy = randint(0,9)
        
        if ("%s,%s")%(posx,posy) in teamShipCords:
            self.place(teamShipCords)
        else:            
            if self.angle == 0: 
                if (posy + self.lenShip) < 10:
                    i = 0    
                    self.shipCords = []
                    for i in range(0, self.lenShip):
                        self.shipCords.append('%d,%d' % (posx, posy + i))
                
                elif (posy - self.lenShip) >= 0:
                    i = 0
                    self.shipCords = []
                    for i in range(0, self.lenShip):
                        self.shipCords.append('%d,%d' % (posx, posy - i))
                
                else:
                    self.place(teamShipCords)
            
            else:
                if (posx + self.lenShip) < 10:
                    i = 0
                    self.shipCords = []
                    for i in range(0, self.lenShip):
                        self.shipCords.append('%d,%d' % (posx + i, posy))
                        
                elif (posx - self.lenShip) >=0:
                    i = 0    
                    self.shipCords = []
                    for i in range(0, self.lenShip):
                        self.shipCords.append('%d,%d' % (posx - i, posy))
                        
                else:
                    self.place(teamShipCords)
                
            for cord in self.shipCords:
                if cord in teamShipCords:
                    return 'REPEAT' #Avoids recursion
            #print self.shipCords
                        
    def damage(self):
        self.currentDamage += 1
         
        if self.currentDamage >= self.lenShip:
            self.sunk()
      
    def sunk(self):
        self.wasSunk = True         
    


