import re

l = []
file1 = open('data/exo39', 'r')
lines = file1.readlines()

code = []

def convert(c):
    if c == ".":
        return 0
    else:
        return 1

for c in lines[0][:-1]:
    code.append(convert(c))


grid = []
for line in lines[2:-1]:
    row = []
    for c in line[:-1]:
        row.append(convert(c))
    grid.append(row)

def binToInt(s):
    r = 0
    for c in s:
        r = r*2 + int(c)
    return r


def enhancePixel(M,i,j,code,modulo):
    r = 0
    p = 1    
    n = len(M)
    m = len(M[0])
    for a in range(-1,2):
        for b in range(-1,2):
            if i-a >= 0 and i-a < n and j-b >= 0 and j-b < m:
                #print(i-a,j-b,p*M[i-a][j-b])
                r += p*M[i-a][j-b]
            elif modulo == 1:
                r += p
            p *= 2
    #print(r)
    return code[r]


#M = [[1,0,0,1,0],[1,0,0,0,0],[1,1,0,0,1],[0,0,1,0,0],[0,0,1,1,1]]
#print(enhancePixel(M,-1,1,code))

def enhanceImage(g,modulo):
    global code
    n = len(g)
    m = len(g[0])
    r = []
    for i in range(-1,n+1):
        row = []
        for j in range(-1,m+1):
            row.append(enhancePixel(g,i,j,code,modulo))
        r.append(row)
    return r

def count(M):
    r = 0
    for i in range(len(M)):
        for j in range(len(M[0])):
            r += M[i][j] == 1
    return r
def countbis(M):
    r = 0
    for i in range(len(M)):
        for j in range(len(M[0])):
            r += M[i][j] == 0
    return r

def pp(M):
    for l in M:
        for e in l:
            print(e,end=" ")
        print()
    print()


for i in range(25):
    grid = enhanceImage(enhanceImage(grid,0),1)
print(count(grid))

