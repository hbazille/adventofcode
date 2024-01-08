
class Hail:
    def __init__(self, p, v):
        self.px = p[0]
        self.py = p[1]
        self.pz = p[2]
        self.vx = v[0]
        self.vy = v[1]
        self.vz = v[2]
    
    
def parseline(s):
    t = s.split("@")
    return Hail(tuple(map(lambda x : int(x.strip()), t[0].split(","))), tuple(map(lambda x : int(x.strip()), t[1].split(",")))) 
                 
def iscolinear(dx1, dy1, dx2, dy2):
    return dx1 * dy2 == dx2 * dy1
                 
def intersect2d(h1, h2):
    x1, y1, dx1, dy1 = h1.px, h1.py, h1.vx, h1.vy
    x2, y2, dx2, dy2 = h2.px, h2.py, h2.vx, h2.vy
    if iscolinear(dx1, dx2, dy1, dy2):
        return (-1, -1, 0, 0)
    k2 = (y1 - y2 + dy1 * (x2 - x1) / dx1) / (dy2 - dx2 * dy1 / dx1)
    k1 = ((x2 - x1) + k2 * dx2) / dx1
    return (k1, k2, x1 + k1 * dx1, y1 + k1 * dy1)             
    

def isinterin(h1, h2, l, u):
    k1, k2, xi, yi = intersect2d(h1, h2)
    return k1 >= 0 and k2 >= 0 and l <= xi <= u and l <= yi <= u
                 
if __name__ == "__main__":
    l = [parseline(s.strip()) for s in open('data/day24', 'r').readlines()]
    n = len(l)
    lb = 200000000000000
    ub = 400000000000000
    print(sum(isinterin(l[i], l[j], lb, ub) for i in range(n) for j in range(i+1, n)))
