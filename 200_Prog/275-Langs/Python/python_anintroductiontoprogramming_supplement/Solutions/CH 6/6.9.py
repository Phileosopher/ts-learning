# 6.9 Blackjack player
from random import *
# This is only one way to do this, and it does make a few assumptions.
# Reasonable assumptions seem like a fair thing to allow.
class player:
    def __init__(self, hold, money, ante):
        self.hold = hold
        self.money = money
        self.hand = []
        self.ante = ante
        self.ace = False
        self.id = 1

    def new_hand (self, up, down):
        if up == 1:
            self.hand = [1, down]
            self.ace = True
        elif down == 1:
            self.hand = [1, up]
            self.ace = True
        else:
            self.hand = [up, down]
        self.money =self.money - self.ante
        print ("Player ", self.id, "holds", self.hand, " has $", self.money)

    def hit (self):
        sum = 0
        sum1 = 10
        for i in range (0, len(self.hand)):
            sum = sum + self.hand[i]
            if self.ace:
                sum1 = sum1 + self.hand[i]
            else:
                sum1 = 22
        print ("HIT on ", sum, sum1)
        if sum < sum1:
            score = sum
        else:
            score = sum1
        if (sum>19 and sum<22) or (sum1>19 and sum1<22): return False
        if score < self.hold:
            return True
        else:
            return False

    def card (self, c):
        print ("Player ", self.id, "gets a ", c)
        sum = 0
        sum1 = 10
        self.hand = self.hand + [c,]
        for i in range (0, len(self.hand)):
            sum = sum + self.hand[i]
            if self.ace:
                sum1 = sum1 + self.hand[i]
            else:
                sum1 = 22
        if sum>21 and sum1>21:
            print ("Busted")
        else:
            print ("Score now ", end="")
            if sum<=21:
                print (sum, end="")
            if sum1<21:
                print (sum1, end="")
            print()

p = player (16, 1000, 5)

for i  in range (1, 10):
    c1 = randrange (1, 14)
    if c1 >= 10:
        c1 = 10
    c2 = randrange (1, 14)
    if c2 > 10:
        c2 = 10
    p.new_hand (c1, c2)
    c = input()
    while p.hit():
        c = randrange (1,14)
        if c>10:
            c = 10
        p.card(c)
        q = input()




