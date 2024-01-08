
def hexatodec(c):
    r = 0
    for s in c:
        r = r * 16 + "0123456789abcdef".index(s)
    return r   
        
def parseline(l, d):
    c = l.strip().split()[2][2:-1]
    return d[c[-1]], hexatodec(c[:-1])


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
        r += yi1 * (xi1 - xi)
    return r, b
    
if __name__ == "__main__":
    d = {"0" : "R", "1" : "D", "2" : "L", "3" : "U"}
    t = [parseline(l, d) for l in open('data/day18', 'r').readlines()]
    r, b = shoelace(getpoints(t))
    print(r + b // 2 + 1)
