import numpy as np


def parse(line):
    t = line.split(",")
    return int(t[0]), int(t[1]), int(t[2])

def nb(grid):
    w, h, l = grid.shape
    c = 0
    for x in range(w):
        for y in range(h):
            for z in range(l):
                if grid[x,y,z]:
                    prevc = c
                    for dx,dy,dz in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]:
                        if (0 <= x + dx < w and 0 <= y + dy < h and 0 <= z + dz < l) and grid[x+dx,y+dy,z+dz]:
                            c += 1
    return c


if __name__ == '__main__':
    file1 = open('data/day18', 'r')
    lines = file1.readlines()
    n = len(lines) - 1
        
    grid = np.zeros((22, 22, 22), dtype = bool)
    for line in lines[:-1]:
        x, y, z = parse(line[:-1])
        grid[x,y,z] = True
    print( 6*n - nb(grid))
