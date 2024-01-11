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


class Blizzard:
    def __init__(self, pos, dx, dy):
        self.x = pos[0]
        self.y = pos[1]
        self.dx = dx
        self.dy = dy
        
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + "," + str(self.dx) + "," + str(self.dy) + ")"
        
    def update(self, limx, limy):
        self.x += self.dx
        self.y += self.dy
        if 0 == self.x:
            self.x = limx - 1
        elif self.x == limx:
            self.x = 1
        elif self.y == 0:
            self.y = limy - 1
        elif self.y == limy:
            self.y = 1
    
    
class Grid:
    def __init__(self, limx, limy):
        self.limx = limx
        self.limy = limy
        self.blines = []
        self.bcols = []
        for _ in range(limx):
            self.bcols.append([])
        for _ in range(limy):
            self.blines.append([])
        
    def update(self):
        for l in self.blines:
            for b in l:
                b.update(self.limx, self.limy)
        for c in self.bcols:
            for b in c:
                b.update(self.limx, self.limy)
    
    
def BFS(grid, st, end):
    q = Queue()
    q.enqueue(st)
    q2 = Queue()
    c = 0
    while not q.isempty():
        p = q.dequeue()
        j, i = p
        collision = False
        if i == st[1] or not (any(b.y == i for b in grid.bcols[j]) or any(b.x == j for b in grid.blines[i])):
            for (dj, di) in [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)]:
                je, ie = j + dj, i + di
                if je == end[0] and ie == end[1]:
                    return c + 1
                if 0 < ie < grid.limy and 0 < je < grid.limx and (je, ie) not in q2.elements or (ie == st[1] and je == st[0]):
                    q2.enqueue((je, ie))
        if q.isempty():
            c += 1
            grid.update()
            q, q2 = q2, q

        
if __name__ == '__main__':
    file = open('data/day24', 'r')
    lines = file.readlines()
    m = len(lines) - 2
    n = len(lines[0]) - 2
    grid = Grid(n, m)
    st = (1, 0)
    end = (grid.limx -1, grid.limy)
    for i in range(len(lines) - 1):
        for j in range(len(lines[i])):
            c = lines[i][j]
            if c == ">":
                grid.blines[i].append(Blizzard((j,i), 1, 0))
            elif c == "<":
                grid.blines[i].append(Blizzard((j,i), -1, 0))
            elif c == "^":
                grid.bcols[j].append(Blizzard((j,i), 0, -1))
            elif c == "v":
                grid.bcols[j].append(Blizzard((j,i), 0, 1))
    p1 = BFS(grid, st, end)
    grid.update()
    p2 = BFS(grid, end, st)
    grid.update() 
    p3 = BFS(grid, st, end)
    print(p1 + p2 + p3)     
    
