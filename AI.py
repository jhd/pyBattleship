#Copyright	Jonathan Hennessy-doyle 2012
#		jonathanhennessydoylety@gmail.com
#Licenced under the GPL v2

from random import randint
class AI(object):
    def __init__(self):
        pass
    def AIshot(self, shots, hits): 
        if hits == []: #If no hits just guess
            return randint(0,9), randint(0,9)
        for runner in hits: #Shoot around previous hits
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
            if right not in shots:              
                return (int(runner[0]) + 1), runner[2]
        return randint(0,9), randint(0,9) #If no shots around hits are untaken return to guessing 
