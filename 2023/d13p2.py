


def parseblock(t, i):
    b = []
    l = t[i].strip()
    while l != "":
        b.append(l)
        i += 1
        l = t[i].strip()
    return b, i + 1
    
def dist(l1, l2):
    return sum(0 if l1[i] == l2[i] else 1 for i in range(len(l1)))    
    
def transpose(m):
    r = []
    for j in range(len(m[0])):
        r.append([])
        for i in range(len(m)):
            r[j].append(m[i][j])
    return r

def verify(b, a, v):
    n = len(b)
    ra = min(a, n - a)
    return all(v == i or b[a + i] == b[a - i - 1] for i in range(ra))


def symh(b):
    n = len(b)
    for i in range(n - 1):
        for j in range(i + 1, n, 2):
            diff = dist(b[i], b[j])
            v = (i + j) // 2 + 1
            if diff == 1 and verify(b, v, v - i - 1):
                return v
    return 0
            
def score(b):
    v = symh(b)
    if v != 0:
        return 100 * v
    return symh(transpose(b))
  
if __name__ == "__main__":
    t = open('data/day13', 'r').readlines()
    i, s = 0, 0
    while i < len(t):
        b, i = parseblock(t, i)
        s += score(b)
    print(s)
