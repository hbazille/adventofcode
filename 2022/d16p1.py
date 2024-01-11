file1 = open('data/day16', 'r')
lines = file1.readlines()
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


def parse(line, dictval, dictfollow):
    t = line.split()
    name = t[1]
    v = int(t[4][5:-1])
    dictval[name] = v
    l = []
    l.append(t[-1])
    i = -2
    while "valve" not in t[i]:
        l.append(t[i][:-1])
        i -= 1
    dictfollow[name] = l
    if v != 0:
        return name
    
def dist(i, dictval, dictfollow, interesting):
    d = {}
    d[i] = 0
    q = Queue()
    q.enqueue(i)
    while not q.isempty():
        i = q.dequeue()
        for j in dictfollow[i]:
            if j not in d.keys():
                d[j] = d[i] + 1
                q.enqueue(j)
    dint = {}
    for e in interesting:
        dint[e] = d[e]
    return dint
    
def _dfs(i, inte, val, dist, vis, t, cur):
    if t <= 0:
        return cur
    vis[i] = True
    v = val[i]*(t)
    best = cur + v
    for j in inte:
        if not vis[j]:
            dij = dist[i][j]
            best = max(best,  _dfs(j, inte, val, dist, vis, t - dij - 1, cur + v))
    vis[i] = False
    return best
    
def dfs(start, interesting, dictval, dictdist):
    vis = {}
    for e in interesting:
        vis[e] = False
    return _dfs(start, interesting, dictval, dictdist, vis, 30, 0)
        
    
if __name__ == "__main__":    
    dictval = {}
    dictfollow = {}
    interesting = ["AA"]
    for line in lines[:-1]:
        s = parse(line, dictval, dictfollow)
        if s != None:
            interesting.append(s)
            
    dictdist = {}
    for i in interesting:
        dictdist[i] = dist(i, dictval, dictfollow, interesting)

    print(dfs("AA", interesting, dictval, dictdist))

