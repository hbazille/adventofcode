
def parseline(l):
    t = l.strip().split()
    return t[0], int(t[1])


def getpoints(t):
    li = [(-1, -1)]
    i, j = -1, -1
    d = {"U" : (-1, 0), "D" : (1, 0), "L" : (0, -1), "R" : (0, 1)}
    for l in t:
        w, k = l
        di, dj = d[w]
        if di != 0:
            i += k * di
        else:
            j += k * dj
        li.append((i, j))
    return li


def shoelace(l):
    r = 0
    n = len(l)
    b = 0
    for i in range(n):
        xi, yi = l[i]
        xi1, yi1 = l[(i+1) % n]
        b += abs(yi1 - yi) + abs(xi1 - xi)
        r += yi * (xi1 - xi)
    return r, b
    
if __name__ == "__main__":
    t = [parseline(l) for l in open('data/day18', 'r').readlines()]
    r, b = shoelace(getpoints(t))
    print(r + b // 2 + 1)
