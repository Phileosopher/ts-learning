# Exercise 4.7
from random import *

def ping (p):
    if random() < p:
        return True
    return False

def pong (p):
    if random() < p:
        return True
    return False

def gameover (s1, s2):
    if (s1<11 and s2<11) or (abs(s1-s2)<2):
        return False
    return True

pongscore = 0
pingscore = 0
pping = 0.9
ppong = 0.93

while not gameover (pingscore, pongscore):
    for i in (1,2,3,4):      # Pong serves 4 times
        while True:              # A point
            if not ping(pping):
                pongscore = pongscore + 1;
                break
            if not pong(ppong):
                pingscore = pingscore + 1;
                break
        print ("Ping:", pingscore, "Pong", pongscore)
        if gameover (pingscore, pongscore):
            break
    for i in (1,2,3,4):      # Ping serves 4 times
        while True:              # A point
            if not pong(ppong):
                pingscore = pingscore + 1;
                break
            if not ping(pping):
                pongscore = pongscore + 1;
                break
        print ("Ping:", pingscore, "Pong", pongscore)
        if gameover (pingscore, pongscore):
            break