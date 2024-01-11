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


def _dfs(i, inte, val, dist, t, mask, cache):
    if t <= 0:
        return 0
    idi = dictid[i]
    v = cache[idi][t][mask//2]
    if v >= 0:
        return v
    v = val[i] * t
    best = 0
    for j in inte:
        bit = 1 << dictid[j]
        if mask & bit:
            dij = dist[i][j]
            best = max(best,  _dfs(j, inte, val, dist, t - dij - 1, mask - bit, cache))
    cache[idi][t][mask//2] = best + v
    return best + v
    
def dfs(start, interesting, dictval, dictdist, mask, cache):
    return _dfs(start, interesting, dictval, dictdist, 26, mask, cache)


if __name__ == "__main__":    
    file1 = open('data/exo31', 'r')
    lines = file1.readlines()
        
    dictval = {}
    dictfollow = {}
    interesting = ["AA"]
    dictid = {}
    dictid["AA"] = 0
    c = 1
    for line in lines[:-1]:
        s = parse(line, dictval, dictfollow)
        if s != None:
            dictid[s] = c   
            c += 1
            interesting.append(s)

    dictdist = {}
    for i in interesting:
        dictdist[i] = dist(i, dictval, dictfollow, interesting)

    best = 0
    mask = (1 << len(interesting))//2
    cache = []

    for _ in range(len(interesting)):
        cache.append([])
        for _ in range(27):
            cache[-1].append([-1] * mask)
       
    best = max([dfs("AA", interesting, dictval, dictdist, m * 2, cache) + dfs("AA", interesting, dictval, dictdist, (mask - m - 1) * 2, cache) for m in range(mask//2)])
    print(best)

