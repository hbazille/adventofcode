import re

l = []
file1 = open('data/exo37', 'r')
lines = file1.readlines()

def parseline(l):
    t = l[:-1].split(",")
    return int(t[0]),int(t[1]),int(t[2])


def product(M,X):
    r = [0,0,0]
    for i in range(3):
        for k in range(3):
            r[i] += M[i][k]*X[k]
    return(r[0],r[1],r[2])
    
scanners = [[]]
completed = 0
i = 1
while completed < 29:
    line = lines[i]
    if len(line)<3:
        completed += 1
        if completed < 29:
            scanners.append([])
        i += 2
    else:
        scanners[completed].append(parseline(line))
        i += 1
nb = 0
for s in scanners:
    nb += len(s)
#print(nb)
def sq(x):
    return x*x
def distance(u,v):
    return sq(u[0]-v[0]) + sq(u[1]-v[1]) + sq(u[2]-v[2])

def similarity(l1,l2):
    r = 0
    for e in l1:
        if e in l2:
            r += 1
    return r

def computesim(sm1,sm2):
    r = 0
    for s in sm1:
        for t in sm2:
            if similarity(s,t)==12:
                r += 1
    return r
distancesmap = []    

for s in scanners:
    scanmap = []
    for i in range(len(s)):
        scanmap.append([])
        for j in range(len(s)):
            scanmap[i].append(distance(s[i],s[j]))
    distancesmap.append(scanmap)

nbs = 0
similars = []

for i in range(len(distancesmap)):
    for j in range(i+1,len(distancesmap)):
        if computesim(distancesmap[i],distancesmap[j]) == 12:
            similars.append((i,j))
#print(len(similars))

#similars = [(0, 6), (0, 14), (0, 24), (1, 2), (1, 15), (2, 22), (2, 24), (3, 15), (4, 11), (5, 13), (5, 16), (5, 26), (5, 28), (7, 26), (8, 18), (8, 21), (9, 12), (9, 13), (9, 26), (10, 26), (11, 18), (11, 21), (13, 18), (13, 24), (15, 22), (16, 17), (16, 18), (19, 25), (19, 27), (20, 28), (23, 28), (27, 28)]

vertices = [i for i in range(29)]
edges = [[]for i in range(29)]

for e in similars:
    edges[e[0]].append(e[1])
    edges[e[1]].append(e[0])


def _DFS(visited,src,e,l):
    visited[src] = True
    for adj in e[src]:
        if not visited[adj]:
            _DFS(visited,adj,e,l)
            l.append((src,adj))
def DFS(v,e):
    visited = [False]*len(v)
    l = []    
    _DFS(visited,0,e,l)
    return l


similars = DFS(vertices,edges)


def computeSimPoints(sm1,sm2):
    l = []
    for i in range(len(sm1)):
        s = sm1[i]
        for j in range(len(sm2)):
            t = sm2[j]
            if similarity(s,t)>10:
                l.append((i,j))
    return l


def diff(v1,v2):
    return (v2[0]-v1[0],v2[1]-v1[1],v2[2]-v1[2])

def add(v1,v2):
    return (v2[0]+v1[0],v2[1]+v1[1],v2[2]+v1[2])


def getPoint(start,Minv,diff):
    return add(start,product(Minv,diff))

nbs = len(scanners)
scannerPosition = [[None for i in range(len(scanners))] for j in range(len(scanners))]
for i in range(nbs):
    scannerPosition[i][i] = (0,0,0)

dict = {}
#print(len(scanners))
for s in similars:
    n0 = s[0]
    n1 = s[1]
    s0 = distancesmap[s[0]]
    s1 = distancesmap[s[1]]
    #if n0 == 0 and n1 == 13:
    #    print(len(scanners[0]),len(scanners[13]))
    l = computeSimPoints(s0,s1)
    M = [[0,0,0],[0,0,0],[0,0,0]]
    Minv = [[0,0,0],[0,0,0],[0,0,0]]
    diff0  = diff(scanners[s[0]][l[0][0]],scanners[s[0]][l[1][0]])
    diff1  = diff(scanners[s[1]][l[0][1]],scanners[s[1]][l[1][1]])
    for i in range(3):
        for j in range(3):
            if diff0[i] == diff1[j]:
                Minv[i][j] = 1
                M[j][i] = 1
            elif diff0[i] == -diff1[j]:
                Minv[i][j] = -1
                M[j][i] = -1
    p0 = scanners[s[0]][l[0][0]]
    p0prime = scanners[s[1]][l[0][1]]
    for i in range(len(scanners[s[1]])):

        piprime = scanners[s[1]][i]
        ptransformed = getPoint(p0,Minv,diff(p0prime,piprime))
        if ptransformed not in scanners[n0]:
            scanners[n0].append(ptransformed)
    for i in range(nbs):
        posScani = scannerPosition[n1][i]
        if posScani != None:
            scannerPosition[n0][i] = getPoint(p0,Minv,diff(p0prime,posScani))

def manhattan(p1,p2):
    v = diff(p1,p2)
    return abs(v[0])+abs(v[1])+abs(v[2])

biggest = 0
for e in scannerPosition[0]:
    for f in scannerPosition[0]:
        v = manhattan(e,f)
        biggest = max(v,biggest)
print(biggest) 
"""
    print(scanners[s[0]][l[0][0]], scanners[s[0]][l[1][0]])
    print(M)
    print(product(Minv,diff1),diff0)
"""
