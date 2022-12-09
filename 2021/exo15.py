import re

l = []
file1 = open('data/exo15', 'r')
lines = file1.readlines()

r = 0

for line in lines:
    l = line.split("|")
    out = l[1].split()
    for e in out:
        r += (len(e) in [2,3,4,7])

print(r)

