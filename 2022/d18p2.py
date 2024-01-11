import numpy as np
from collections import deque


class Queue:
    def __init__(self):
        self.elements = deque()
    def enqueue(self, elt):
        self.elements.append(elt)
    def dequeue(self):
        return self.elements.popleft()
    def isempty(self):
        return len(self.elements) == 0


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
                        if not ((0 <= x + dx < w and 0 <= y + dy < h and 0 <= z + dz < l) and grid[x+dx,y+dy,z+dz]):
                            c += 1
    return c
    
def fillside(grid, gridw, visited, q):
    w, h, l = grid.shape
    for x in range(w):
        for y in range(h):
            if not grid[x,y,0]:
                gridw[x,y,0] = True
                q.enqueue((x,y,0))
            if not grid[x,y,l-1]:
                gridw[x,y,l-1] = True
                q.enqueue((x,y,l-1))
            visited[x,y,0] = True
            visited[x,y,l-1] = True
            for z in range(l):
                if not grid[x,0,z]:
                    gridw[x,0,z] = True
                    q.enqueue((x,0,z))
                if not grid[x,h-1,z]:
                    gridw[x,h-1,z] = True
                    q.enqueue((x,h-1,z))
                if not grid[0,y,z]:
                    gridw[0,y,z] = True
                    q.enqueue((0,y,z))
                if not grid[w-1,y,z]:
                    gridw[w-1,y,z] = True
                    q.enqueue((w-1,y,z))
                visited[x,0,z] = True
                visited[x,h-1,z] = True
                visited[0,y,z] = True
                visited[w-1,y,z] = True


def fill(grid, gridw):
    w,h,l = grid.shape
    q = Queue()
    visited = np.zeros((w,h,l), dtype = bool)
    fillside(grid, gridw, visited, q)
    while not q.isempty():
        x,y,z = q.dequeue()
        for dx,dy,dz in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]:
            if (0 <= x + dx < w and 0 <= y + dy < h and 0 <= z + dz < l) and not visited[x+dx,y+dy,z+dz] and not grid[x+dx,y+dy,z+dz]:
                q.enqueue((x+dx, y+dy, z+dz))
                visited[x+dx,y+dy,z+dz] = True
                gridw[x+dx, y+dy, z+dz] = True


if __name__ == '__main__':
    file1 = open('data/exo35', 'r')
    lines = file1.readlines()
    n = len(lines) - 1
    K = 22
    grid = np.zeros((K, K, K), dtype = bool)
    gridw = np.zeros((K, K, K), dtype = bool)
    for line in lines[:-1]:
        x, y, z = parse(line[:-1])
        grid[x,y,z] = True
    fill(grid, gridw)
    gridw = np.invert(gridw)
    print(nb(gridw))
