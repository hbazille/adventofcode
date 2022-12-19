import re

l = []
file1 = open('data/exo9', 'r')
lines = file1.readlines()

grid = []
for i in range(1000):
    grid.append([0]*1000)

def fill(g,i1,j1,i2,j2):
    di = i2 - i1
    dj = j2 - j1
    if di == 0:
        for j in range(min(j1,j2),max(j1,j2)+1):
            g[i1][j] += 1
    elif dj == 0:
        for i in range(min(i1,i2),max(i1,i2)+1):
            g[i][j1] += 1
    else:
        ki,kj = 0,0
        udi = di//abs(di)
        udj = dj//abs(dj)
        while abs(ki)<=abs(di):
            g[i1+ki][j1+kj] += 1
            ki += udi
            kj += udj

def count(g):
    r = 0
    for i in range(len(g)):
        for j in range(len(g[0])):
            r += g[i][j] > 1   
    return r

for line in lines:
    liste = line.split()
    i1,j1,i2,j2 = int(liste[0]),int(liste[1]),int(liste[2]),int(liste[3])
    fill(grid,i1,j1,i2,j2)
            

print(count(grid))

