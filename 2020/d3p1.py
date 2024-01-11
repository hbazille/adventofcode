import numpy as np


    
if __name__ == "__main__":
    file = open('data/day3', 'r')
    lines = file.readlines()
    n, m = len(lines) - 1, len(lines[0]) - 1
    grid = np.zeros((n, m), dtype = bool)
    for i in range(n):
        l = lines[i]
        for j in range(m):
            if l[j] == "#":
                grid[i, j] = True
    px, py, c = 0, 0, 0
    while px < n:
        c += grid[px, py]
        px += 1 
        py  = (py + 3) % m
    print(c)
    
