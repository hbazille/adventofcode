from functools import cmp_to_key


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


def testremove(l):
    n = len(l)
    d = set()
    for i in range(n):
        li = []
        bi = l[i]
        j = 0
        while j < i and len(li) < 2:
            bj = l[j]
            if bj.pmax[2] == bi.pmin[2] and bi.intersect(bj) > 0:
                li.append(j)
            j += 1
        if len(li) == 1:
            d.add(li[0])
    return n - len(d)
            
                 
if __name__ == "__main__":
    l = []
    for line in open('data/day22', 'r').readlines():
        parseline(line.strip(), l)
    l.sort(key=(lambda x : x.pmin[2]))
    fall(l)
    print(testremove(l))
