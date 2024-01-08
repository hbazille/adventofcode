class Heap:
    def __init__(self, sizeMax):
        self.heap = [None]
        self.index = [-1]*sizeMax        
    
    def is_empty(self):
        return len(self.heap) == 1

    def _moveUp(self, pos):
        (val, elt) = self.heap[pos]
        while (pos > 1) and (val < self.heap[pos//2][0]):
            self.heap[pos] = self.heap[pos//2]
            self.index[self.heap[pos][1]] = pos
            pos = pos // 2
        self.heap[pos] = (val, elt)
        self.index[elt] = pos
                
    def push(self, elt, val):
        self.heap.append((val, elt))
        self.index[elt] = len(self.heap)-1
        self._moveUp(len(self.heap)-1)
    
    def update(self, elt, newVal):
        pos = self.index[elt]
        if pos == -1:
            self.heap.append((newVal, elt))
            pos = len(self.heap)-1
            self.index[elt] = pos
        else:
            self.heap[pos] = (newVal, elt)
        self._moveUp(pos)
        
    def pop(self):
        e = self.heap[1]
        self.index[e[1]] = -1
        (val, elt) = self.heap[len(self.heap)-1]
        self.heap.pop()
        if not self.is_empty():
            n = len(self.heap)-1
            ok = False
            i = 1    
            while (i <= n // 2) and not ok:
                j = 2 * i
                if (j + 1 <= n) and (self.heap[j+1][0] < self.heap[j][0]):
                    j = j + 1
                if val > self.heap[j][0]:
                    self.heap[i] = self.heap[j]
                    self.index[self.heap[i][1]] = i
                    i = j
                else:
                    ok = True
            self.heap[i] = (val, elt)
            self.index[self.heap[i][1]] = i
            
        return e


def convert(i, j, s, c, n):
    return i * n + j + n*n*(4*c+s)

def convertback(v, n):
    j = v % n
    v = v // n
    i = v % n
    v = v // n
    s = v % 4
    c = v // 4
    return i, j, s, c

def codetodir(co):
    if co == 0:
        return -1, 0
    if co == 1:
        return 0, 1
    if co == 2:
        return 1, 0
    return 0, -1

def create(h, d, i, j, s, c, v, n):
    e = convert(i, j, s, c, n)
    h.update(e, v) 
    d[i][j][s][c] = v

def shortest(t, n):
    h = Heap(n * n * 44)
    d = []
    for i in range(n):
        d.append([])
        for j in range(n):
            d[i].append([])
            for s in range(4):
                d[i][j].append([])
                for c in range(11):
                    d[i][j][s].append(1000000)
    create(h, d, 0, 1, 1, 1, int(t[0][1]), n)
    create(h, d, 1, 0, 2, 1, int(t[1][0]), n)
    cp = 0
    while not h.is_empty():
        sc, v = h.pop()
        cp += 1
        i, j, s, c = convertback(v, n)
        if (i, j) == (n-1, n-1):
            return sc
        if c < 10:     
            di, dj = codetodir(s)
            alti, altj = i + di, j + dj
            if 0 <= alti < n and 0 <= altj < n:
                dv = sc + int(t[alti][altj])
                if dv < d[alti][altj][s][c+1]:
                    create(h, d, alti, altj, s, c + 1, dv, n)
        if c < 4:
            continue
        for alts in [s-1, s+1]:
            alts = alts % 4
            di, dj = codetodir(alts)
            alti, altj = i + di, j + dj
            if 0 <= alti < n and 0 <= altj < n:
                dv = sc + int(t[alti][altj])
                if dv < d[alti][altj][alts][1]:
                    create(h, d, alti, altj, alts, 1, dv, n)
    return -1

if __name__ == "__main__":
    t = open('data/day17', 'r').readlines()
    n = len(t)
    print(shortest(t, n))
