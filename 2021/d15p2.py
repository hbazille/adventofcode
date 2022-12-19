import re

l = []
file1 = open('data/exo29', 'r')
lines = file1.readlines()

data = []
for l in lines[:-1]:
    ligne = []
    for e in l[:-1]:
        ligne.append(int(e))
    data.append(ligne)

class Heap:
    def __init__(self, sizeMax):
        self.heap = [None]
        self.index = [-1]*sizeMax        
    
    def is_empty(self):
        return len(self.heap) == 1

    def _moveUp(self, pos):
        (val, elt) = self.heap[pos]
        while (pos > 1) and (val < self.heap[pos//2][0]):
            self.heap[pos] = self.heap[pos//2]
            self.index[self.heap[pos][1]] = pos
            pos = pos // 2
        self.heap[pos] = (val, elt)
        self.index[elt] = pos
        
        
    def push(self, elt, val):
        self.heap.append((val, elt))
        self.index[elt] = len(self.heap)-1
        self._moveUp(len(self.heap)-1)
    
    def update(self, elt, newVal):
        pos = self.index[elt]
        if pos == -1:
            self.heap.append((newVal, elt))
            pos = len(self.heap)-1
            self.index[elt] = pos
        else:
            self.heap[pos] = (newVal, elt)
        self._moveUp(pos)
    
        
    def pop(self):
        e = self.heap[1]
        self.index[e[1]] = -1
        (val, elt) = self.heap[len(self.heap)-1]
        self.heap.pop()
        if not self.is_empty():
            n = len(self.heap)-1
            ok = False
            i = 1    
            while (i <= n // 2) and not ok:
                j = 2 * i
                if (j + 1 <= n) and (self.heap[j+1][0] < self.heap[j][0]):
                    j = j + 1
                if val > self.heap[j][0]:
                    self.heap[i] = self.heap[j]
                    self.index[self.heap[i][1]] = i
                    i = j
                else:
                    ok = True
            self.heap[i] = (val, elt)
            self.index[self.heap[i][1]] = i
            
        return e



def creategrid(data,n,m):
    res = [[0 for j in range(5*m)] for i in range(5*n)]
    for i in range(n):
        for j in range(m):
            for a in range(5):
                for b in range(5):
                    res[a*n+i][b*m+j] = convert(data[i][j],a,b)
    return res

            
def convert(e,i,j):
    v = e+i+j
    r = v%9
    if r == 0:  
        return 9
    else:
        return r

n = len(data)
m = len(data[0])

data = creategrid(data,n,m)
n = len(data)
m = len(data[0])

res = [[float('inf') for j in range(m)] for i in range(n)]
mask = [[True for j in range(m)] for i in range(n)]
res[0][0] = 0
heap = Heap(n*m)

def encode(i,j):
    global m
    return i*m+j

def decode(k):
    global m
    return (k//m, k%m)

def findminheap(grid,heap):
    if heap.is_empty():
        return None
    return heap.pop()

def update(data,grid,heap,istart,jstart,iend,jend,n,m):
    vstart = grid[istart][jstart]
    if iend >= 0 and iend < n and jend >= 0 and jend < m:
        vadd = data[iend][jend]
        vtotal = vstart + vadd
        if vtotal < grid[iend][jend]:
            grid[iend][jend] = vtotal
            heap.update(encode(iend,jend),vtotal)
            

def dijkstra(data,grid,heap,n,m):
    st = 0,0
    while st != None and st != (m-1,n-1):
        update(data,grid,heap,st[0],st[1],st[0]+1,st[1],n,m)
        update(data,grid,heap,st[0],st[1],st[0]-1,st[1],n,m)
        update(data,grid,heap,st[0],st[1],st[0],st[1]+1,n,m)
        update(data,grid,heap,st[0],st[1],st[0],st[1]-1,n,m)
        st = findminheap(grid,heap)
        if st != None:
            st = decode(st[1])
        #print(st)
    return grid[n-1][m-1]

print(dijkstra(data,res,heap,n,m))
