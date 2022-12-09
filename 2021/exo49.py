import re
import itertools

l = []
file1 = open('data/exo49', 'r')
lines = file1.readlines()

grid = []
for line in lines[:-1]:
    l = []
    for e in line[:-1]:
        if e == "v":
            l.append("S")
        elif e == ">":
            l.append("E")
        else:
            l.append(" ")
    grid.append(l)
            
def checkMoveSouth(grid,i,j):
    n = len(grid)
    return grid[(i+1)%n][j] == " "
    
def checkMoveEast(grid,i,j):
    m = len(grid[0])
    return grid[i][(j+1)%m] == " "
    
def updateSouth(grid):
    n = len(grid)
    m  = len(grid[0])
    hasChanged = False
    for j in range(m):
        first = grid[0][j]
        i = 0
        while i < n-1:
            if grid[i][j] == "S" and checkMoveSouth(grid,i,j):
                hasChanged = True
                grid[i][j] = " "
                grid[i+1][j] = "S"
                i += 1
            i += 1
        if i == n-1 and grid[i][j] == "S" and first == " ":
            grid[i][j] = " "
            grid[0][j] = "S"
            hasChanged = True
    return hasChanged
     
     
def updateEast(grid):
    n = len(grid)
    m  = len(grid[0])
    hasChanged = False
    for i in range(n):
        first = grid[i][0]
        j = 0
        while j < m-1:
            if grid[i][j] == "E" and checkMoveEast(grid,i,j):
                hasChanged = True
                grid[i][j] = " "
                grid[i][j+1] = "E"
                j += 1
            j += 1
        if j == m-1 and grid[i][j] == "E" and first == " ":
            grid[i][j] = " "
            grid[i][0] = "E"
            hasChanged = True
    return hasChanged
     
def pp(g):
    for l in g:
        for e in l:
            print(e,end=" ")
        print()
    print()
    
t = 0
b1, b2 = True, True
while t < 1000 and (b1 or b2):
    #if t%10 == 0:
    #    print(t)
    b1 = updateEast(grid)
    b2 = updateSouth(grid)
    t += 1
   
print(t)


