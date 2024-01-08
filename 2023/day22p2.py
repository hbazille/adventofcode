
from utils import graph, queue

class Brick:
    def __init__(self, pmin, pmax):
        self.pmin = pmin
        self.pmax = pmax
            
    def intersect(self, brick):
        # brick below self
        x_overlap = max(0, min(self.pmax[0], brick.pmax[0]) - max(self.pmin[0], brick.pmin[0]));
        y_overlap = max(0, min(self.pmax[1], brick.pmax[1]) - max(self.pmin[1], brick.pmin[1]));
        if x_overlap * y_overlap > 0:
            return brick.pmax[2]
        return 0
     
    def movez(self, c):
        xm, ym, zm = self.pmin
        xM, yM, zM = self.pmax
        newzM = c + zM - zm
        self.pmin = xm, ym, c
        self.pmax = xM, yM, newzM 
     
         
def parseline(b, l):
    t = b.split("~")
    l.append(Brick(tuple(map(lambda x : int(x), t[0].split(",") )), tuple(map(lambda x : int(x) + 1, t[1].split(",") )) ))
    

def fall(l):
    n = len(l)
    for i in range(n):
        c = 1
        bi = l[i]
        for j in range(i):
            c = max(c, bi.intersect(l[j]))
        bi.movez(c)


def buildgraph(l):
    n = len(l)
    G = graph.Graph(n + 1)
    G.adjlists[n] = [n]
    for i in range(n):
        bi = l[i]
        j = 0
        if bi.pmin[2] == 1:
            G.adjlists[n].append(i)
        else:
            while j < i:
                bj = l[j]
                if bj.pmax[2] == bi.pmin[2] and bi.intersect(bj) > 0:
                    G.adjlists[j].append(i)
                j += 1
    return G
     
            
def indeg(G):
    n = G.order
    ind = [0] * n
    for i in range(n):
         for j in G.adjlists[i]:
            ind[j] += 1
    return ind
     
         
def tryr(G, i, ind):
    q = queue.Queue()
    q.enqueue(i)
    c = -1
    while not q.isempty():
        i = q.dequeue()
        c += 1
        for j in G.adjlists[i]:
            ind[j] -= 1
            if ind[j] == 0:
                q.enqueue(j)
    return c
     
         
if __name__ == "__main__":
    l = []
    for line in open('data/day22', 'r').readlines():
        parseline(line.strip(), l)
    l.sort(key=(lambda x : x.pmin[2]))
    fall(l)
    G = buildgraph(l)
    ind = indeg(G)
    print(sum(tryr(G, i, ind.copy()) for i in range(G.order - 1)))
