from random import *
from math import *

def genpop (population_size):
    pop = []
    for i in range(0, population_size):
        p = [1.0*randrange(-10, 10),  1.0*randrange(-10, 10)]
        pop = pop + [p,]
    return pop

def objective (m, b):  # x,y are data points
    global xdata, ydata
    sum = 0.0
    for i in range (0, len(xdata)):
        sum = sum + (m*xdata[i]+b-ydata[i])  # Difference between line and point
    return abs(sum)

def eval ():
    global population, npop
    e = []
    for i in range (0, npop):
        c = population[i]
        r = objective(c[0], c[1])
        e = e + [r,]
    return e

def sort (p, e):
    for i in range (0, len(e)):
        for j in range (i, len(e)):
            if e[i] > e[j]:
                t = e[i]; e[i] = e[j]; e[j] = t
                q = p[i]; p[i] = p[j]; p[j] = q

def mutate (m):
    global pmut, population
    for i in range (int(m), len(population)):
        c = population[i]
        if random () < pmut:         # Mutate the m parameter
            c[0] = c[0] + random()/10.0-0.05
        if random () < pmut:        # Mutate the b parameter
            c[1] = c[1] + random()/10.0-0.05
        population[i] = c

def crossover (m):
    global population, pcross
    for i in range (m, len(population)):
        if random () < pcross:
            k = randrange(m, len(population))
            w = randrange (0, 1)
            c = population[i]
            cc = population[k]
            t = c[w]; c[w] = cc[w]; cc[w] = (t+cc[w])/2

def select (p):
    global npop, keep
    n = int(npop*keep)
    for i in range (n, len(p)):
        j = randrange (0, n)
        p[i] = list(p[j])

# Read the data and create lists of points xdata and ydata
f = open ("treedata.txt", "r")
s = f.readline ()
xdata = ()
ydata = ()

while s != "":
    for i in range (1,len(s)):
        if s[i] == ",":
            break
    x = float(s[0:i-1])
    y = float(s[i+1:])
    xdata = xdata + (x,)
    ydata = ydata + (y,)
    s = f.readline()



npop = 200       # Population size
keep = 0.1       # Percent of population that stays each generation
generation = 1
pcross = .4
pmut = 0.2

population = genpop (npop)   # Generate the initial population

print (population)
laste = 0.0
for i in range (0, 3000):
  e = eval ()  # Evaluate all individuals
  if e[0] < 0.00001: break
  sort (population, e)  # Sort on evaluation
  print (i, "Best this iteration is ", population[0], " at ", e[0])
  select (population)  # select the to percent, copy the rest.
  mutate (20)     # do mutations
  crossover (20)  # Do crossover
  laste = e[0]

print (objective (0.0, 0.0))
