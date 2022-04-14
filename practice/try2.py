import random
import matplotlib.pyplot as plt
from matplotlib import cm, projections
from matplotlib.ticker import LinearLocator
from operator import attrgetter
import numpy as np
from rastigans2 import Ras

##########
# for reproduction using parents
##########

POPSIZE = 10
HALFPOP = (POPSIZE//2)-1

#plt.ion()
fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize=(16, 9))

# Make data.
X = np.arange(-5, 5, 0.2)
Y = np.arange(-5, 5, 0.2)
X, Y = np.meshgrid(X, Y)
Z = 20 + (X**2) + (Y**2) - 10*(np.cos((2*np.pi*X)) + np.cos((2*np.pi*Y)))


# Plot the surface.
surf = ax.plot_surface(X, Y, Z, alpha=.2, cmap=cm.winter,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-100, 100)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colours.
fig.colorbar(surf, shrink=0.5, aspect=5)

def calcFitness( popArray ):
    for i in range(POPSIZE):
        popArray[i].calc()

#find the total fitness of entire pop
def getMaxFitness( popArray ):
    max = 0.0
    for i in range(POPSIZE):
        max += popArray[i].fitness
        return max

def orderPop( popArray ):
    s = sorted(popArray, key=attrgetter('fitness'))
    return s

def removeScatters( popArray ):
    for i in popArray:
        ax.scatter(i.x1, i.x2, i.fitness, color='red', alpha=1).remove()

def addFittest( pa ):
    #pa = list of pop in order of fitness
    newPA = []
    for i in range(HALFPOP, -1, -1):
        #adds fittest half to mating pool.
        x1 = pa[i].get_x1()
        x2 = pa[i].get_x2()
        newMember = Ras(x1, x2)
        newPA.append(newMember)
    return newPA

def newMP( pa ):
    mp = addFittest(pa)
    for i in mp:
        i.mutate()
    return mp

def newPop( popArray):
    #order pop, higher index = fitter
    popArray = orderPop(popArray)
    #matingPool = array of 5 fittest candidates *2
    matingPool = newMP(popArray)
    matingPool.extend(addFittest(popArray))
    calcFitness(matingPool)

    #Currently:
    #order pop by fitness
    #take fittest 5, mutate
    #take fittest 5 (again) and add to list of mutated version
    #repeat

    #I want:
    #Order arry (fittest is first)
    #Take fitness scores of all of pop 
    #Normalise- scores = decimal values so total normal fitness equals 1 (call this probability?)
    #problem is this, atm lowest fitness score = better. For improved 
    #Need to inverse the probabilites. I.E if normalised fitness = 0.1 ... then prob = 0.9
    
    for i in matingPool:
        print(i.x1, i.x2, i.fitness)

    return matingPool


#array of population
popArray = []

#initialise & show population
for i in range(POPSIZE):
    x1 = random.uniform(-4.0, 4.0)
    x2 = random.uniform(-4.0, 4.0)
    data = Ras(x1, x2)
    popArray.append(data)

#draw on graph
calcFitness(popArray)
scArray = []
for i in popArray:
    scArray.append(ax.scatter(i.x1, i.x2, i.fitness, color='red', alpha=1))
    
plt.show()
print("original pop")
for i in popArray:
        print(i.x1, i.x2, i.fitness)


for i in range (10):
    print("population version: ", (i+1))
    popArray = newPop(popArray)
    
    

removeScatters(popArray)


plt.draw()