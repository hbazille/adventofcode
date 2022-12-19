import re

l = []
file1 = open('data/exo11', 'r')
lines = file1.readlines()

line = lines[0].split(",")

l = [0]*9
for e in line:
    l[int(e)] += 1

def next(l):
    lres = [0]*9
    lres[8] = l[0]
    lres[6] = l[0]
    for i in range(1,9):
        lres[i-1] += l[i]
    return lres

def sum(l):
    r = 0
    for e in l:
        r += e
    return r

for i in range(256):
    l = next(l)
print(sum(l))
