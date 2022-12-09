import sys

l = []
file1 = open('data/exo1', 'r')
lines = file1.readlines()


for line in lines:
    l.append(int(line[:-1]))

i = 0
n = len(l)
r = 0

while(i<n-3):
    prev = l[i]+l[i+1]+l[i+2]
    cur = l[i+1]+l[i+2]+l[i+3]
    r += prev < cur
    i += 1

print(r)
