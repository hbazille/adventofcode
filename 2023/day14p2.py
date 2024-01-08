def move(t, i, j, di, dj, n):
    ti = i + di
    tj = j + dj
    while n > ti >= 0 and n > tj >= 0 and t[ti][tj] == ".":
        ti += di
        tj += dj
    ti -= di
    tj -= dj
    t[i][j], t[ti][tj] = t[ti][tj], t[i][j]
  
def tiltn(t, n):
    for i in range(n):
        for j in range(n):
            if t[i][j] == "O":
                move(t, i, j, -1, 0, n)
  
def tilts(t, n):
    for i in range(n-1, -1, -1):
        for j in range(n):
            if t[i][j] == "O":
                move(t, i, j, 1, 0, n)

def tiltw(t, n):
    for i in range(n):
        for j in range(n):
            if t[i][j] == "O":
                move(t, i, j, 0, -1, n)
  
def tilte(t, n):
    for i in range(n):
        for j in range(n-1, -1, -1):
            if t[i][j] == "O":
                move(t, i, j, 0, 1, n)

def buildt(t, n):
    r = []
    for i in range(n):
        r.append([])
        for j in range(n):
            r[i].append(t[i][j])
    return r


def cycle(t, n):
    tiltn(t, n)
    tiltw(t, n)
    tilts(t, n)
    tilte(t, n)

def seen(t, n, d, c):
    ts = str(t)
    try:
        return d[ts]
    except:
        d[ts] = c


def loadt(t, n):
    return sum( ((n-i) * sum(1 for j in range(n) if t[i][j] == "O")) for i in range(n))
    

if __name__ == "__main__":
    t = open('data/day14', 'r').readlines()
    c, n = 0, len(t)
    k, d = 1000000000, {}
    t = buildt(t, n)
    while seen(t, n, d, c) == None:
        c += 1
        cycle(t, n)
    v = seen(t, n, d, c)
    c += ((k - c) // (c - v) ) * (c - v)
    while c < k:
        c += 1
        cycle(t, n)
    print(loadt(t, n))
    
