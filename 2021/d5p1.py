import re

l = []
file1 = open('data/day5', 'r')
lines = file1.readlines()

grid = []
for i in range(1000):
    grid.append([0]*1000)

def fill(g,i1,j1,i2,j2):
    for i in range(i1,i2+1):
        for j in range(j1,j2+1):
            g[i][j] += 1

def count(g):
    r = 0
    for i in range(len(g)):
        for j in range(len(g[0])):
            r += g[i][j] > 1   
    return r

for line in lines:
    liste = line.split()
    i1,j1,i2,j2 = int(liste[0]),int(liste[1]),int(liste[2]),int(liste[3])
    if i1 == i2:
        if j1<j2:
            fill(grid,i1,j1,i2,j2)
        else:
            fill(grid,i2,j2,i1,j1)
    elif j1==j2:
        if i1<i2:
            fill(grid,i1,j1,i2,j2)
        else:
            fill(grid,i2,j2,i1,j1)
            

print(count(grid))

