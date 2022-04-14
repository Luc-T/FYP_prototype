from cgi import test
import random

from numpy import append
from rastigans import Ras
from operator import attrgetter

POPSIZE = 10
HALFPOP = (POPSIZE//2)-1

def newPop():
    mp = []
    for i in range(HALFPOP+1):
        x1 = random.uniform(-4.0, 4.0)
        x2 = random.uniform(-4.0, 4.0)
        data = Ras(x1, x2)
        mp.append(data)
    return mp

testArray = []
for i in range(POPSIZE):
    x1 = random.uniform(-4.0, 4.0)
    x2 = random.uniform(-4.0, 4.0)
    testDat = Ras(x1, x2)
    testArray.append(testDat)

""" for i in testArray:
    print(i.x1, i.x2)

print("Calc")
for i in testArray:
    i.calc()
    print(i.fitness) """


#find fitness of each member of pop
x = 0
for i in testArray:
    x+=1
    i.calc()
    print("Position: ", x ,"fitness: ", i.fitness)

#sort testArray
testArray = sorted(testArray, key=attrgetter('fitness'))


""" testArray[-1].calc()
print(testArray[-1].fitness) """

print("NOW SORTED!!!")
x = 0
for i in testArray:
    x+=1
    print("Position: ", x ,"fitness: ", i.fitness)



REPLACE = (POPSIZE//2)-1
testDat = Ras(-10, -10)
#POPSIZE / 2 = 5
#add 5 new members to pop
matingPool = newPop()

print("Taken fittest five . . . ")
for i in range(REPLACE, -1, -1):
    #then add fittest 5 to pop
    matingPool.append(testArray[i])
    testArray[i].calc()
    print("Position: ", i ,"fitness: ", testArray[i].fitness)

x = 0


print("mating pool")
print(HALFPOP)
for i in matingPool:
    x+=1
    i.calc()
    print("Position: ", x ,"fitness: ", i.fitness)