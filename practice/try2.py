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

#pick a parent based on fitness
def pickOne( pA ):
    index = 0
    r = random.random()
    while (r > 0):
        r = r - pA[index].get_prob()
        index +=1

    index -= 1
    return pA[index]

def newPop( popArray):
    #order pop, higher index = fitter
    popArray = orderPop(popArray)
    sum = 0
    for i in popArray:
        sum += i.get_fitness()
    #create normalised probability score
    for i in popArray:
        i.set_prob((i.get_fitness() / sum))

    j = 0
    for i in range((POPSIZE-1), HALFPOP, -1):
        
        temp = popArray[i].get_prob()
        popArray[i].set_prob(popArray[j].get_prob())
        popArray[j].set_prob(temp)
        j+=1
    
    newMember = pickOne(popArray)
    

    #matingPool = array of 5 fittest candidates *2
    matingPool = newMP(popArray)
    matingPool.extend(addFittest(popArray))
    calcFitness(matingPool)

    #To Do:
    #create function to use takeOne
    #select two parents, make child, fill list of new Pop
    #Also, fix the prob, not accurate I believe
    
    total = 0
    for i in popArray:
        print(i.x1, i.x2, i.fitness, "Prob: ", i.get_prob())
        total += i.get_prob()

    print("Sum of prob = ", total)
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

for i in popArray:
    ax.scatter(i.x1, i.x2, i.fitness, color='red', alpha=1)
    
plt.show()
print("original pop")
for i in popArray:
        print(i.x1, i.x2, i.fitness)


for i in range (1):
    print("population version: ", (i+1))
    popArray = newPop(popArray)
    
