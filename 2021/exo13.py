import re

l = []
file1 = open('data/exo13', 'r')
lines = file1.readlines()

line = lines[0].split(",")

for e in line:
    l.append(int(e))

l.sort()
length = len(l)//2


def distance(l,m):
    r = 0
    for e in l:
        r += abs(e-m)
    return r

print(min(distance(l,l[length]),distance(l,l[length+1])))


