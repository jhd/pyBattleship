#Copyright	Jonathan Hennessy-doyle 2012
#		jonathanhennessydoylety@gmail.com
#Licenced under the GPL v2

class ship(object):
    
    def __init__(self, team, stype, teamShipCords):
        self.lenship = 0
        self.currentdamage = 0
        self.team = team
        self.type = stype
        self.wassunk = False
        self.shipcords = []
    
    def place(self, stype, posx, posy, teamShipCords):
        from random import randint
        self.angle = randint(0,1)
        #print  stype, posx, posy, self.angle
        if stype == "SS" :
            self.lenship = 3
        elif stype == "CR":
            self.lenship = 3
        elif stype == "BS":
            self.lenship = 4
        elif stype == "CA":
            self.lenship = 5
        elif stype == "DD":
            self.lenship = 2
        else: # Invalid ship
            self.lenship = -1
            
        self.cords = '%d,%d,%d' % (posx, posy, self.angle)
        
        if self.angle == 0: #TODO VERY wasteful and inefficient, replace ASAP
            if (posy + self.lenship) < 10:
                i = 0    
                for i in range(0, self.lenship):
                    self.shipcords.append('%d,%d' % (posx, posy + i))
            
            elif (posx + self.lenship) < 10:
                i = 0
                for i in range(0, self.lenship):
                    self.shipcords.append('%d,%d' % (posx + i, posy))
            
            else:
                self.place(stype, randint(0,9), randint(0,9), teamShipCords)
        
        else:
            if (posx + self.lenship) < 10:
                i = 0
                for i in range(0, self.lenship):
                    self.shipcords.append('%d,%d' % (posx + i, posy))
                    
            elif (posy + self.lenship) < 10:
                i = 0    
                for i in range(0, self.lenship):
                    self.shipcords.append('%d,%d' % (posx, posy + i))
                    
            else:
                self.place(stype, randint(0,9), randint(0,9), teamShipCords)
            
        for cord in self.shipcords:
            if cord in teamShipCords:
                return "REPEAT" #Avoids recursion
        
        #if a == 1:
           # self.place(stype, randint(0,9), randint(0,9), teamShipCords)
        #else:
           # pass
        #if self.shipcords in teamShipCords:
           # print "In logs: ", self.shipcords 
            #self.place(stype, randint(0,9), randint(0,9), teamShipCords)
                
     
    def sunk(self, stype, team):
        #print "%s of %s team sunk!" % (stype, team)
        #print "%s %s sunk was called" % (team, stype)
        self.wassunk = True
        
    # damage depreciated in favour of sunkCheck
    def damage(self):
        self.maxdamage = self.lenship #Not in __init__ as self.lenship not known until after self.place call
        self.currentdamage += 1
         
        #print self.currentdamage, self.maxdamage
        if self.currentdamage >= self.maxdamage:
            self.sunk(self.type, self.team)
    
    def sunkCheck(self):
        self.maxdamage = self.lenship
        if self.currentdamage >= self.maxdamage: #current damage set manually in control.py
            self.sunk(self.type, self.team)
          
    

