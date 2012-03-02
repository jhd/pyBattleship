#Copyright	Jonathan Hennessy-doyle 2012
#		jonathanhennessydoylety@gmail.com
#Licenced under the GPL v2

from random import randint
from shipclass import ship
from AI import AI

redShips = []
blueShips =[]
#blue
blueCarrier = ship("blue", "CA", blueShips)

blueBattleship = ship("blue","BS", blueShips)

blueSub = ship("blue", "SS", blueShips)

blueCruiser = ship("blue", "CR", blueShips)

blueDestroyer = ship("blue", "DD", blueShips)
    
if blueCarrier.place("CA", randint(0,9), randint(0,9), blueShips) == "REPEAT":
    blueCarrier.place("CA", randint(0,9), randint(0,9), blueShips)
blueShips = sum([blueShips, blueCarrier.shipcords], []) #Join a list of lists to a list

if blueBattleship.place("BS", randint(0,9), randint(0,9), blueShips) == "REPEAT":
    blueBattleship.place("BS", randint(0,9), randint(0,9), blueShips)
blueShips = sum([blueShips, blueBattleship.shipcords], [])

if blueSub.place("SS", randint(0,9), randint(0,9), blueShips) == "REPEAT":
    blueSub.place("SS", randint(0,9), randint(0,9), blueShips)
blueShips = sum([blueShips, blueSub.shipcords], [])

if blueCruiser.place("CR", randint(0,9), randint(0,9), blueShips) == "REPEAT":
    blueCruiser.place("CR", randint(0,9), randint(0,9), blueShips)
blueShips = sum([blueShips, blueCruiser.shipcords], [])

if blueDestroyer.place("DD", randint(0,9), randint(0,9), blueShips) == "REPEAT":
    blueDestroyer.place("DD", randint(0,9), randint(0,9), blueShips)
blueShips = sum([blueShips, blueDestroyer.shipcords], [])
#endblue
#red
redCarrier = ship("red", "CA", redShips)

redBattleship = ship("red","BS", redShips)

redSub = ship("red", "SS", redShips)

redCruiser = ship("red", "CR", redShips)

redDestroyer = ship("red", "DD", redShips)
    
if redCarrier.place("CA", randint(0,9), randint(0,9), redShips) == "REPEAT":
    redCarrier.place("CA", randint(0,9), randint(0,9), redShips)
redShips = sum([redShips, redCarrier.shipcords], [])

if redBattleship.place("BS", randint(0,9), randint(0,9), redShips) == "REPEAT":
    redBattleship.place("BS", randint(0,9), randint(0,9), redShips)
redShips = sum([redShips, redBattleship.shipcords], [])

if redSub.place("SS", randint(0,9), randint(0,9), redShips) == "REPEAT":
    redSub.place("SS", randint(0,9), randint(0,9), redShips)
redShips = sum([redShips, redSub.shipcords], [])

if redCruiser.place("CR", randint(0,9), randint(0,9), redShips) == "REPEAT":
    redCruiser.place("CR", randint(0,9), randint(0,9), redShips)
redShips = sum([redShips, redCruiser.shipcords], [])

if redDestroyer.place("DD", randint(0,9), randint(0,9), redShips) == "REPEAT":
    redDestroyer.place("DD", randint(0,9), randint(0,9), redShips)
redShips = sum([redShips, redDestroyer.shipcords], [])
#endred
def checkinput(xguess, yguess):
    if xguess >=0 and xguess <=9 and yguess >=0 and yguess <=9:
        return True
    else:
        return False
        
def humanInput(team):
    print "%s\'s turn:" % team
    xguess = raw_input("x-cord:")
    if xguess == "shots":
        if team == "red":
            print redShots
            xguess = raw_input("x-cord:")
            
        else:
            print blueShots
            xguess = raw_input("x-cord:")
    if xguess == "hits":
        if team == "red":
            for test in redShots:
                if test in blueShips:
                    print test
        else:
            for test in blueShots:
                if test in redShips:
                    print test   
        xguess = raw_input("x-cord:")
                     
    if xguess == "sunk":
        if team == "red":
            if blueBattleship.wassunk == True:
                print "BS sunk"                  
            if blueCarrier.wassunk == True:
                print "CA sunk"
            if blueCruiser.wassunk == True:
                print "CR sunk"
            if blueSub.wassunk == True:
                print "SS sunk"
            if blueDestroyer.wassunk == True:
                print "DD sunk"
        
        else:
            if redBattleship.wassunk == True:
                print "BS sunk"                  
            if redCarrier.wassunk == True:
                print "CA sunk"
            if redCruiser.wassunk == True:
                print "CR sunk"
            if redSub.wassunk == True:
                print "SS sunk"
            if redDestroyer.wassunk == True:
                print "DD sunk"      
        xguess = raw_input("x-cord:")
                
    yguess = raw_input("y-cord:")
    if xguess.isdigit() and yguess.isdigit() and int(xguess) in range(0,10) and int(yguess) in range(0,10):
        return (xguess, yguess)
    else:
        print "Please enter intergers between 0 and 9"
        return humanInput(team)

def victoryConditions():
    if blueDestroyer.wassunk == True:
        if blueSub.wassunk == True:
            if blueCruiser.wassunk == True:
                if blueBattleship.wassunk == True:
                    if blueCarrier.wassunk == True:
                        return "Red" #red victory
                        
    if redDestroyer.wassunk == True:
        if redSub.wassunk == True:
            if redCruiser.wassunk == True:
                if redBattleship.wassunk == True:
                    if redCarrier.wassunk == True:
                        return "Blue" #red victory        
    else:
        return "Continue" #no victor                    

                            
#while checkinput(humaninput()) == False :
#    pass
blueShots = []
redShots = []
redAI = AI()
blueAI = AI()
def shot(team, race):
    if race == "human":
        xguess, yguess = humanInput(team)
    
    else:
        if team == "blue": 
            blueHits = []
            for runner in blueShots:
                if runner in redShips:
                    blueHits.append(runner)
            xguess, yguess = blueAI.AIshot(blueShots, blueHits)
        else:
            redHits = []
            for runner in redShots:
                if runner in blueShips:
                    redHits.append(runner)
            xguess, yguess = redAI.AIshot(redShots, redHits)
    if team == "blue":    
        if ('%d,%d' % (int(xguess), int(yguess))) in blueShots:
            if race == "human":
                print "Shot already taken"
            shot(team, race)
            
        else:
            if "%d,%d" % (int(xguess), int(yguess)) in redShips:
                print "Ship hit! %d, %d" % (int(xguess), int(yguess))# damage ship
                blueShots.append("%d,%d" % (int(xguess), int(yguess)))
            else:
                blueShots.append("%d,%d" % (int(xguess), int(yguess)))
                
    else:
        if ('%d,%d' % (int(xguess), int(yguess))) in redShots:
            if race == "human":
                print "Shot already taken"
            shot(team, race)
            
        else:
            if "%d,%d" % (int(xguess), int(yguess)) in blueShips:
                print "Ship hit! %d, %d" % (int(xguess), int(yguess))# damage ship
                redShots.append("%d,%d" % (int(xguess), int(yguess)))
            #print "Ship hit! %d, %d" % (int(xguess), int(yguess))
            else:
                redShots.append("%d,%d" % (int(xguess), int(yguess)))
            #print "%d,%d" % (int(xguess), int(yguess))
                
#shot("blue", "human")
#shot("red", "computer")
#print blueBattleship.shipcords
#print blueSub.shipcords
#print blueDestroyer.shipcords
#print blueCarrier.shipcords
#print blueCruiser.shipcords

#print blueShips
#print redShips
humanDict = ['human', 'Human', 'h', 'H']
player1race = raw_input("Player 1 >")
if player1race in humanDict:
    player1race = 'human'
    player1name = raw_input("Name for player 1>")
    
player2race = raw_input("Player 2 >")
if player2race in humanDict:
    player2race = 'human'
    player2name =raw_input('Name for player 2>') 
    
#TODO difficulty setting
#TODO game modes
while victoryConditions() != "Red" and victoryConditions() != "Blue": #Main loop
    #print blueShots
    #print redShips
    #print 'DD', redDestroyer.wassunk
    #print 'CR', redCruiser.wassunk
    #print 'SS', redSub.wassunk
    #print 'BS', redBattleship.wassunk
    #print 'CA', redCarrier.wassunk
    shot("blue", player1race)
    shot("red", player2race)
    rCHits = 0
    rCRHits = 0
    rBHits = 0
    rDHits = 0
    rSHits = 0
    bCHits = 0
    bCRHits = 0
    bBHits = 0
    bDHits = 0
    bSHits = 0
    for test in blueShots: #tests for hits
        if test in redShips:
            if test in redCarrier.shipcords:
                rCHits += 1
                redCarrier.currentdamage = rCHits
                redCarrier.sunkCheck()
            elif test in redBattleship.shipcords:
                rBHits += 1
                redBattleship.currentdamage = rBHits
                redBattleship.sunkCheck()
            elif test in redSub.shipcords:
                rSHits += 1
                redSub.currentdamage = rSHits
                redSub.sunkCheck()
            elif test in redCruiser.shipcords:
                rCRHits += 1
                redCruiser.currentdamage = rCRHits
                redCruiser.sunkCheck()
            elif test in redDestroyer.shipcords:
                rDHits += 1
                redDestroyer.currentdamage = rDHits
                redDestroyer.sunkCheck()
    for test in redShots:
        if test in blueShips:
            if test in blueCarrier.shipcords:
                bCHits += 1
                blueCarrier.currentdamage = bCHits
                blueCarrier.sunkCheck()
            elif test in blueBattleship.shipcords:
                bBHits += 1
                blueBattleship.currentdamage = bBHits
                blueBattleship.sunkCheck()
            elif test in blueSub.shipcords:
                bSHits += 1
                blueSub.currentdamage = bSHits
                blueSub.sunkCheck()
            elif test in blueCruiser.shipcords:
                bCRHits += 1
                blueCruiser.currentdamage = bCRHits
                blueCruiser.sunkCheck()
            elif test in blueDestroyer.shipcords:
                bDHits += 1
                blueDestroyer.currentdamage = bDHits
                blueDestroyer.sunkCheck()
    #print 'CA:' ,rCHits     
    #print 'CR:', rCRHits
    #print 'BS', rBHits 
    #print 'DD', rDHits 
    #print 'SS:', rSHits ,'\n' 
    #print 'DD', redDestroyer.wassunk
    #print 'CR', redCruiser.wassunk
    #print 'SS', redSub.wassunk
    #print 'BS', redBattleship.wassunk
    #print 'CA', redCarrier.wassunk, '\n\n'
    #print redShots
    #print blueShips
    #print blueShots
         
winner = victoryConditions()
if winner == "blue" and player1race == "human":
    print player1name + "won!"
elif winner == "red" and player2race == "human":
    print player2name + "won!"
else:
    print winner + ' team wins!' 

#print redShots
#print blueShips
#print blueShots
#print redShips
