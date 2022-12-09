import re

l = []
file1 = open('data/exo7', 'r')
lines = file1.readlines()

bingonumbers = []

grids = []
gridscheck = []


def sumUnmarked(N,M):
    r = 0
    for i in range(len(N)):
        for j in range(len(N[0])):
            if not M[i][j]:
                r += int(N[i][j])
    return r

def update(N,M,p):
    i = 0
    while i<len(N):
        j = 0
        while j < len(M):
            if N[i][j] == p:
                M[i][j] = True
                return i,j 
            j += 1
        i += 1
    return None

def checkH(M,i):
    j = 0
    while j < len(M[0]) and M[i][j] == True:
        j += 1
    return j >= len(M[0])


def checkV(M,j):
    i = 0
    while i < len(M) and M[i][j] == True:
        i += 1
    return i >= len(M)


def firstline(line):    
    li = line.split(",")
    return li

bingonumbers = firstline(lines[0][:-1])

def nextgrid(lines,i,g,gc):
    j = 0
    m = []
    c = []
    while j<5:
        c.append([False]*5)
        m.append(lines[i+j][:-1].split())
        j += 1 
    g.append(m)
    gc.append(c)

i = 2
while i < len(lines):
    nextgrid(lines,i,grids,gridscheck)
    i += 6

def bingo(bingonumbers,grids,gridscheck):
    for b in bingonumbers:
        for i in range(len(grids)):
            grid = grids[i]
            gridcheck = gridscheck[i]
            res = update(grid,gridcheck,b)
            if res != None:
                checkvg = checkV(gridcheck,res[1])
                checkhg = checkH(gridcheck,res[0])
                if checkvg or checkhg:
                    return sumUnmarked(grid,gridcheck)*int(b)
    return 0


print(bingo(bingonumbers,grids,gridscheck))


