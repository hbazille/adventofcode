


def getinfo(t):
    n = len(t)
    gal = []
    el = [False] * n
    ec = [False] * n
    for i in range(n):
        for j in range(n):
            if t[i][j] == "#":
                el[i] = True
                ec[j] = True
                gal.append((i, j))
    return gal, [i for i in range(n) if not el[i]], [i for i in range(n) if not ec[i]]
    
def normalize(g1, g2):
    (g1i, g1j), (g2i, g2j) = g1, g2
    g1i, g2i = min(g1i, g2i), max(g1i, g2i)
    g1j, g2j = min(g1j, g2j), max(g1j, g2j)
    return g1i, g2i, g1j, g2j
    
def dist(g1, g2, el, ec):
    g1i, g2i, g1j, g2j = normalize(g1, g2)
    return (g2i - g1i + g2j - g1j 
        + sum(1 for e in el if (e - g1i) * (e - g2i) < 0)
        + sum(1 for e in ec if (e - g1j) * (e - g2j) < 0))
    
def alldist(gal, el, ec):
    n = len(gal)
    return sum(sum(dist(gal[i], gal[j], el, ec) for j in range(i+1,n)) for i in range(n-1))
  
if __name__ == "__main__":
    t = open('data/day11', 'r').readlines()
    print(alldist(*getinfo(t)))
