import re

l = []
#file1 = open('data/exo39', 'r')
#lines = file1.readlines()

p1 = 4
p2 = 10

s1 = 0
s2 = 0

dv = 1
t = 1
turns = 0

while s1 < 1000 and s2 < 1000:
    dice = dv
    dv = dv%100+1
    dice += dv
    dv = dv%100+1
    dice += dv
    dv = dv%100+1
    dice = dice%10
    if t == 1:
        p1 += dice
        if p1 > 10:
            p1 -= 10
        s1 += p1
    else:
        p2 += dice
        if p2 > 10:
            p2 -= 10
        s2 += p2
    t = 3-t
    turns += 1

#print(s1,s2,3*turns,s1*3*turns,s2*3*turns)
print(s1*3*turns)
