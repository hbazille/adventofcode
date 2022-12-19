import re

l = []
file1 = open('data/exo17', 'r')
lines = file1.readlines()

r = 0
data = []
inputs = []
outputs = []

for line in lines:
    l = line.split()
    data.append(l[0])

#data = ["2day99943210","3987894921","9856789892","8767896789","9899965678"]

n = len(data)
m = len(data[0])


tab = [-1]*(n*m)

def find(n,tab):
    while tab[n] > -1:
        n = tab[n]
    return n

def union(n,m,tab):
    un = find(n,tab)
    um = find(m,tab)
    if un != um:
        vn = tab[un]
        vm = tab[um]
        tab[un] = um
        tab[um] = vn + vm

def enume(i,j,n):
    return i*n+j

points = []
res = 0
sizes = []

for i in range(n):
    for j in range(m):
        v = int(data[i][j])
        if v == 9:
            continue
        valv = enume(i,j,m)
        if i < n-1:
            vi = int(data[i+1][j])
            valvi = enume(i+1,j,m)
            if vi != 9:
                union(valvi,valv,tab)
        if j < m-1:
            vj = int(data[i][j+1])
            valvj = enume(i,j+1,m)
            if vj != 9:
                union(valvj,valv,tab)

tab.sort()
#print(tab)
print(-tab[0]*tab[1]*tab[2])
