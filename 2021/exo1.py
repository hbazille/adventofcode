import sys

l = []
file1 = open('data/exo1', 'r')
lines = file1.readlines()


for line in lines:
    l.append(int(line[:-1]))

i = 0
n = len(l)
r = 0

while(i<n-1):
    prev = l[i]
    cur = l[i+1]
    r += prev < cur
    i += 1

print(r)
