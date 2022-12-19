import re

l = []
file1 = open('data/day15', 'r')
lines = file1.readlines()

data = []
for l in lines[:-1]:
    ligne = []
    for e in l[:-1]:
        ligne.append(int(e))
    data.append(ligne)

n = len(data)
m = len(data[0])

res = [[float('inf') for j in range(m)] for i in range(n)]
mask = [[True for j in range(m)] for i in range(n)]
res[0][0] = 0

changed = True
def findmin(grid,mask):
    minx, miny = -1,-1
    minv = float('inf')
    index = 0
    indexRemove = -1
    for p in mask:
        i,j = p[0],p[1]
        if grid[i][j] < minv:
            minx,miny = i,j
            minv = grid[i][j]
            indexRemove = index
        index += 1
    if minx == -1:
        return minx,miny
    else:
        mask.pop(indexRemove)
        return minx,miny
        
def add(mask,p):
    if p not in mask:
        mask.append(p)

def update(data,grid,mask,istart,jstart,iend,jend,n,m):
    vstart = grid[istart][jstart]
    if iend >= 0 and iend < n and jend >= 0 and jend < m:
        vadd = data[iend][jend]
        if vstart + vadd < grid[iend][jend]:
            grid[iend][jend] = vadd + vstart
            add(mask,(iend,jend))

def dijkstra(data,grid,mask,n,m):
    st = 0,0
    while st != (-1,-1):
        update(data,grid,mask,st[0],st[1],st[0]+1,st[1],n,m)
        update(data,grid,mask,st[0],st[1],st[0]-1,st[1],n,m)
        update(data,grid,mask,st[0],st[1],st[0],st[1]+1,n,m)
        update(data,grid,mask,st[0],st[1],st[0],st[1]-1,n,m)
        st = findmin(grid,mask)
    return grid[n-1][m-1]

print(dijkstra(data,res,mask,n,m))
