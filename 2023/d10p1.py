
def getfill(i, j, c):
    l = []
    if c == "|":
        l.append((i-1, j))
        l.append((i+1, j))
    elif c == "-":
        l.append((i, j - 1))
        l.append((i, j + 1))
    elif c == "L":
        l.append((i - 1, j))
        l.append((i, j + 1))
    elif c == "J":
        l.append((i - 1, j))
        l.append((i, j - 1))
    elif c == "7":
        l.append((i + 1, j))
        l.append((i, j - 1))
    elif c == "F":
        l.append((i + 1, j))
        l.append((i, j + 1))
    #print(i, j, c, l)
    return l
    
def filterp(l, p):
    if p == l[0]:
        return l[1]
    return l[0]    
    
def finds(t, k):
    for i in range(k):
        for j in range(k):
            if t[i][j] == "S":
                return i, j
                
def findloop(t, p):
    c = 1
    i, j = p
    previ, prevj = -1, -1
    for d in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        di, dj = d
        if (i, j) in getfill(i + di, j + dj, t[i+di][j+dj]):
            previ, prevj = i, j
            i, j = i + di, j + dj
            break
    while t[i][j] != "S":
        di, dj = filterp(getfill(i, j, t[i][j]), (previ, prevj))
        i, j, previ, prevj = di, dj, i, j
        c += 1
    return c//2
            
    
    
if __name__ == "__main__":
    t = open('data/day10', 'r').readlines()
    k = len(t)
    si, sj = finds(t, k)
    print(findloop(t, (si, sj)))
