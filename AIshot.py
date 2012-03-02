#Copyright	Jonathan Hennessy-doyle 2012
#		jonathanhennessydoylety@gmail.com
#Licenced under the GPL v2

from random import randint
def AIshot(shots, targets): #TODO better shot taking
    hits = []
    for test in shots: #TODO wasteful, can be held outside loop
        if test in targets:
            hits.append(test)
    return randint(0,9),randint(0,9)
    
