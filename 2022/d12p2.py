file1 = open('data/exo23', 'r')
lines = file1.readlines()


class Node:
    
    def __init__(self,val):
        self.elem = val
        self.next = None
        
        
class Queue:
    
    def __init__(self):
        self.starting_node = None
        self.ending_node = None
        
    def enqueue(self,val):
        node = Node(val)
        if self.ending_node == None:
            self.starting_node = node
            self.ending_node = node
        else:
            self.ending_node.next = node
            self.ending_node = node
    
    def is_empty(self):
        return self.starting_node == None
        
    def dequeue(self):
        if self.starting_node == None:
            raise Exception("Empty queue")
        else:
            val = self.starting_node.elem
            self.starting_node = self.starting_node.next
            if self.starting_node == None:
                self.ending_node = None
            return val


starti, startj = -1, -1
endi, endj = -1, -1
mat = []
grid = []
i = 0
for line in lines[:-1]:
    j = 0
    mat.append([])
    grid.append([])
    for c in line[:-1]:
        if c == "E":
            starti, startj = i, j
            mat[i].append(day12)
        elif c == "S":
            mat[i].append(0) 
        else:
            mat[i].append(ord(c) - ord('a'))
        j += 1
        grid[-1].append(None)
    i += 1


q = Queue()
q.enqueue((starti, startj))
grid[starti][startj] = 0
found_0 = False

while not q.is_empty() and not found_0:
    i, j = q.dequeue()
    v1 = mat[i][j]
    for (di, dj) in [(1,0), (0,1), (-1,0), (0, -1)]:
        i2 = i + di
        j2 = j + dj
        if 0 <= i2 < len(mat) and 0 <= j2 < len(mat[0]):
            v2 = mat[i2][j2]
            if grid[i2][j2] == None and v2 - v1 >= -1:
                grid[i2][j2] = grid[i][j] + 1
                q.enqueue((i2, j2))
                if v2 == 0:
                    found_0 = True
                    endi, endj = i2, j2   
      
      
print(grid[endi][endj])

