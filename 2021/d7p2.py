import re

l = []
file1 = open('data/exo13', 'r')
lines = file1.readlines()

line = lines[0].split(",")

for e in line:
    l.append(int(e))

l.sort()
length = len(l)//2


def d(i,j):
    n = abs(i-j)
    return (n*(n+1))//2

def moyenne(l):
    r = 0
    for e in l:
        r += e
    return r//len(l)

m = moyenne(l)

def distance(l,m):
    r = 0
    for e in l:
        r += d(e,m)
    return r

print(min(distance(l,m),distance(l,m+1)))
