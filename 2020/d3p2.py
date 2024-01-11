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
    total = 1
    for dx, dy in [(1,1), (1,3), (1,5), (1,7), (2,1)]:
        px, py, c = 0, 0, 0
        while px < n:
            c += grid[px, py]
            px += dx 
            py  = (py + dy) % m
        total *= c
    print(total)
    
