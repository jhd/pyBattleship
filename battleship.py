#Copyright Jonathan Hennessy-Doyle 2012
#Licensed under the GPL v2
#Email jonathanhennessydoylety@gmail.com
from shipclass import ship #Data for ships
from random import randint
      
def AIShot(shots, hits):
        if hits == []:
            return randint(0,9), randint(0,9)
        for runner in hits:
            up = (runner[0] + ',' + str(int(runner[2]) + 1) )
            if up  not in shots:
                return runner[0], (int(runner[2]) + 1)
            down = runner[0] + ',' + str(int(runner[2]) - 1) 
            if down not in shots:               
                return runner[0], (int(runner[2]) - 1)
            left = (str(int(runner[0]) - 1)+ ',' + runner[2]  )
            if left  not in shots:              
                return (int(runner[0]) - 1), runner[2]
            right = (str(int(runner[0]) + 1)+ ',' + runner[2]  )
            if right  not in shots:              
                return (int(runner[0]) + 1), runner[2]
        return randint(0,9), randint(0,9)

def askMode():
    salvoDict = ['salvo','1','SALVO','1.']
    singleDict = ['single', '2', 'SINGLE', '2.']
    mode = raw_input('Select game mode:\n1. Salvo\n2. Single-Shot\n> ')
    if mode in salvoDict:
        return 'salvo'
    elif mode in singleDict:
        return 'single'
    else:
        print 'Invalid game mode\n'
        askMode()

def shot(team, shots, hits):
    xpos = raw_input('Xpos > ')
    ypos = raw_input('Ypos > ')
    if xpos.isdigit() and ypos.isdigit() and int(xpos) in range(0,10) and int(ypos) in range(0,10):
        if '%d,%d' % (int(xpos), int(ypos)) not in shots:
            shots.append('%d,%d' % (int(xpos), int(ypos)))
            return xpos, ypos
        else:
            (xpos, ypos) = shot(team, shots, hits)
            return xpos, ypos
    else:
        print 'Xpos and Ypos must be between 0 and 9'
        (xpos, ypos) = shot(team, shots, hits)
        return xpos, ypos
    
def shotCheck(team, xuess, yguess, targets):
    test = ('%s,%s') % (xguess, yguess)
    if test in targets:
        if team == 'blue':  
            if test in redShips:
                blueHits.append(test)
                if test in redCarrier.shipCords:
                    redCarrier.damage()
                elif test in redBattleship.shipCords:
                    redBattleship.damage()
                elif test in redCruiser.shipCords:
                    redCruiser.damage()
                elif test in redSub.shipCords:
                    redSub.damage()
                elif test in redDestroyer.shipCords:
                    redDestroyer.damage()
        
        else:
            if test in blueShips:
                redHits.append(test)
                if test in blueCarrier.shipCords:
                    blueCarrier.damage()
                elif test in blueBattleship.shipCords:
                    blueBattleship.damage()
                elif test in blueCruiser.shipCords:
                    blueCruiser.damage()
                elif test in blueSub.shipCords:
                    blueSub.damage()
                elif test in blueDestroyer.shipCords:
                    blueDestroyer.damage()

def renderBlue():
    output = ''
    for g in range(0, 25):
        print '\n'
    for j in range(0,10):
        k = 9 - j
        output += '%d: ' % (k)
        for i in range(0,10):
            if ('%d,%d' % (i, k)) in blueHits:
                output += 'H'
            elif ('%d,%d' % (i, k)) in blueShots:
                output += 's' 
            else:
                output += '_'    
            output += ' '
        output += '\n' 
    output += '   ^ ^ ^ ^ ^ ^ ^ ^ ^ ^\n'
    output += '   0 1 2 3 4 5 6 7 8 9' 
    print output 
    
def renderRed():
    output = ''
    for g in range(0, 25):
        print '\n'
    for j in range(0,10):
        k = 9 - j
        output += '%d: ' % (k)
        for i in range(0,10):
            if ('%d,%d' % (i, k)) in redHits:
                output += 'H'
            elif ('%d,%d' % (i, k)) in redShots:
                output += 's' 
            else:
                output += '_'    
            output += ' '
        output += '\n' 
    output += '   ^ ^ ^ ^ ^ ^ ^ ^ ^ ^\n'
    output += '   0 1 2 3 4 5 6 7 8 9' 
    print output 
    
def victory():
    if blueDestroyer.wasSunk == True and blueSub.wasSunk == True and blueCruiser.wasSunk == True and blueBattleship.wasSunk == True and blueCarrier.wasSunk == True:
     renderRed()
     return 'red'
#        if blueSub.wasSunk == True:
#            if blueCruiser.wasSunk == True:
#                if blueBattleship.wasSunk == True:
#                    if blueCarrier.wasSunk == True:
                        #return "Red" #red victory
                        
    if redDestroyer.wasSunk == True and redSub.wasSunk == True and redCruiser.wasSunk == True and redBattleship.wasSunk == True and redCarrier.wasSunk == True:
        renderBlue()
        return 'blue'#red victory        
    else:
        return 'NO' #no victor     


gameMode = askMode()
        
humanDict = ['human', 'Human', 'h', 'H']
player1race = raw_input("Player 1 >")
if player1race in humanDict:
    player1race = 'human'
    player1name = raw_input("Name for player 1>")

else:
    player1race = 'computer'
        
player2race = raw_input("Player 2 >")
if player2race in humanDict:
    player2race = 'human'
    player2name =raw_input('Name for player 2>')   

else:
    player2race = 'computer'
              
redShips = []
blueShips = []

redShots = []
blueShots = []

redHits = []
blueHits = []

blueCarrier = ship('CA')
blueCarrier.place(blueShips)
blueShips = sum(blueShips, blueCarrier.shipCords)

blueBattleship = ship('BS')
while blueBattleship.place(blueShips) == 'REPEAT':
    pass
blueShips = sum([blueShips], blueBattleship.shipCords)

blueCruiser = ship('CR')
while blueCruiser.place(blueShips) == 'REPEAT':
    pass
blueShips = sum([blueShips], blueCruiser.shipCords)

blueSub = ship('SS')
while blueSub.place(blueShips) == 'REPEAT':
    pass
blueShips = sum([blueShips], blueSub.shipCords)

blueDestroyer = ship('DD')
while blueDestroyer.place(blueShips) == 'REPEAT':
    pass
blueShips = sum([blueShips], blueDestroyer.shipCords)


redCarrier = ship('CA')
redCarrier.place(redShips)
redShips = sum(redShips, redCarrier.shipCords)

redBattleship = ship('BS')
while redBattleship.place(redShips) == 'REPEAT':
    pass
redShips = sum([redShips], redBattleship.shipCords)

redCruiser = ship('CR')
while redCruiser.place(redShips) == 'REPEAT':
    pass
redShips = sum([redShips], redCruiser.shipCords)

redSub = ship('SS')
while redSub.place(redShips) == 'REPEAT':
    pass
redShips = sum([redShips], redSub.shipCords)

redDestroyer = ship('DD')
while redDestroyer.place(redShips) == 'REPEAT':
    pass
redShips = sum([redShips], redDestroyer.shipCords)

window = screen()
window.main()

while victory() == 'NO':
    renderBlue()
    if player1race == 'human':
        print '%s\'s turn:' % player1name
        xguess, yguess = shot('blue', blueShots, blueHits)
        shotCheck('blue', xguess, yguess , redShips)
    else:
        xguess, yguess = AIShot(blueShots, blueHits)
        blueShots.append('%d,%d' % (int(xguess), int(yguess))) 
        shotCheck('blue', xguess, yguess , redShips)
    
    renderRed()
    if player2race == 'human':
        print '%s\'s turn:' % player2name
        xguess, yguess = shot('red', redShots, redHits)
        shotCheck('red', xguess, yguess , blueShips)
    else:
        xguess, yguess = AIShot(redShots, redHits) 
        redShots.append('%d,%d' % (int(xguess), int(yguess)))
        shotCheck('red', xguess, yguess , blueShips)
if victory() == 'blue' and player1race == 'human':
    print '%s wins!' % player1name
elif victory == 'red' and player2race == 'human':   
    print '%s wins!' % player2name
else:
    print victory(), 'team wins!'
#print redHits, '\n', blueShips
#print redShips, '\n', blueShips
