import numpy as np


K = 5

def initgrid(lines):
    global K
    c = 0
    n, m = len(lines) - 1, len(lines[0]) - 1
    grid = np.zeros((n + 2*K, m + 2*K), dtype = int)
    for i in range(len(lines) -1):
        line = lines[i]
        for j in range(len(line)-1):
            if line[j] == "#":
                grid[i+K, j+K] = True
                c += 1
    return grid, c
        
            
def propose(grid, i, j, k):
    dirn = [(-1, 0), (-1, -1), (-1, 1)]
    dirs = [(1, 0), (1, -1), (1, 1)]
    dirw = [(-1, -1), (0, -1), (1, -1)]
    dire = [(-1, 1), (0, 1), (1, 1)]
    dirt = [dirn, dirs, dirw, dire]
    newi, newj = i, j
    moven = not any(grid[i + di, j + dj] for di, dj in dirt[(k) %4])
    moves = not any(grid[i + di, j + dj] for di, dj in dirt[(k + 1) %4])
    movew = not any(grid[i + di, j + dj] for di, dj in dirt[(k + 2) %4])
    movee = not any(grid[i + di, j + dj] for di, dj in dirt[(k + 3) %4])
    d = [(-1,0), (1, 0), (0, -1), (0, 1)]
    if moven and moves and movew and movee:
        return (i, j), (i, j)
    if moven:
        di, dj = d[k % 4]
        return (i + di, j + dj), (i, j)
    if moves:
        di, dj = d[(k + 1) % 4]
        return (i + di, j + dj), (i, j)
    if movew:
        di, dj = d[(k + 2) % 4]
        return (i + di, j + dj), (i, j)
    if movee:
        di, dj = d[(k + 3) % 4]
        return (i + di, j + dj), (i, j)
    return (i, j), (i, j)    
            
def update(grid, k):
    l = []
    n, m = grid.shape
    for i in range(n):
        for j in range(m):
            if grid[i, j]:
                l.append(propose(grid, i, j, k))
    l.sort()
    next = True
    for k in range(len(l) - 1):
        (newi, newj), (i, j) = l[k]
        (newi2, newj2), (i2, j2) = l[k + 1]
        if newi != newi2 or newj != newj2:
            if next:
                grid[i, j] = False
                grid[newi, newj] = True
            else:
                next = True
        else:
            next = False
    (newi, newj), (i, j) = l[len(l) - 1]
    (newi2, newj2), (i2, j2) = l[len(l) - 2]
    if newi != newi2 or newj != newj2:
        grid[i, j] = False
        grid[newi, newj] = True

def smallest(grid):
    n, m = grid.shape
    lines = np.any(grid, axis = 0)
    columns = np.any(grid, axis = 1)
    i, ie = 0, n-1
    j, je = 0, m-1
    while not lines[i]:
        i += 1
    while not lines[ie]:
        ie -= 1
    while not columns[j]:
        j += 1
    while not columns[je]:
        je -= 1
    return (ie-i+1) * (je-j+1)
    
            
if __name__ == '__main__':
    file = open('data/day23', 'r')
    lines = file.readlines()
    grid, c = initgrid(lines)
    for k in range(10):
        update(grid, k)
    print(grid)
    print(smallest(grid) - c)
