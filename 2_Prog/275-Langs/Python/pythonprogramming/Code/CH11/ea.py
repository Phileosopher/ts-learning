from random import *
from math import *

def genpop (population_size):
    pop = []
    for i in range(0, population_size):
        p = [1.0*randrange(-20, 20),  1.0*randrange(-20, 20)]
        pop = pop + [p,]
    return pop

def ackley (x, y):  # Ackley's function f(0,0) = 0
    sum1 = 0.
    sum2 = 0.
    sum1 = x*x
    sum2 = cos(2.0*pi*x)
    sum1 = sum1 + y*y
    sum2 = sum2 + cos(2.0*pi*y)
    res = -20.0*exp(-0.2*sqrt(sum1/2))
    res = res - exp(sum2/2) + 20 + 2.7182818
    return res

def goldsteinprice (x, y):  # Goldstein-Price function   f(0, -1) = 3
    return (1+(x+y+1)**2 * (19-14*x+3*x*x - 14*y +6*x*y + 3*y*y)) * \
           (30+(2*x-3*y)**2 * (18-32*x+12*x*x+48*y-36*x*y+27*y*y))

def boha (x, y):
    z = x*x + y*y -0.3*cos(3*pi*x) - 0.4*cos(4*pi*y) + 0.7
    return z

def objective (x, y):
    return goldsteinprice (x, y)
#    return boha(x, y)

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
        if random () < pmut:         # Mutate the x parameter
            c[0] = c[0] + random()*10.0-5
        if random () < pmut:        # Mutate the y parameter
            c[1] = c[1] + random()*10.0-5
        population[i] = c

def crossover (m):
    global population, pcross
    for i in range (m, len(population)):
        if random () < pcross:
            k = randrange(m, len(population))
            w = randrange (0, 1)
            c = population[i]
            g1 = c[w]
            cc = population[k]
            g2 = cc[w]
            if (g1>g2): t = g1; g1 = g2; g2 = t  # swap
            c[w] = random()*(g2-g1) + g1
            cc[w] = random()*(g2-g1) + g1

def select (p):
    global npop, keep
    n = int(npop*keep)
    for i in range (n, len(p)):
        j = randrange (0, n)
        p[i] = list(p[j])

npop = 400       # Population size
keep = 0.1       # Percent of population that stays each generation
generation = 1
pcross = .4
pmut = 0.2

population = genpop (npop)   # Generate the initial population

print (population)
for i in range (0, 3000):
  e = eval ()  # Evaluate all individuals
  if e[0] < 0.0001: break
  sort (population, e)  # Sort on evaluation
  print (i, "Best this iteration is ", population[0], " at ", e[0])
  select (population)  # select the top percent, copy the rest.
  mutate (20)     # do mutations
  crossover (20)  # Do crossover

print (objective (0.0, 0.0))
print(objective(3.0, 0.5))