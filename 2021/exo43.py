import re

l = []
file1 = open('data/exo43', 'r')
lines = file1.readlines()


class Cuboid:
    def __init__(self, xmin,xmax,ymin,ymax,zmin,zmax,onoff):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.zmin = zmin
        self.zmax = zmax
        self.onoff = onoff

    def pp(self):
        print(self.xmin,self.xmax,self.ymin,self.ymax,self.zmin,self.zmax,self.onoff)
        

def contains(P1,P2):
    # is P1 in P2
    return P1.xmin >= P2.xmin and P1.xmax <= P2.xmax and P1.ymin >= P2.ymin and P1.ymax <= P2.ymax and P1.zmin >= P2.zmin and P1.zmax <= P2.zmax

def split(P1,P2):
    # splits P1 in parts that are not in P2 
    if P1.xmin < P2.xmin:
        pass

def isIn(p,C):
    return p[0] >= C.xmin and p[0] <= C.xmax and p[1] >= C.ymin and p[1] <= C.ymax and p[2] >= C.zmin and p[2] <= C.zmax


cubes = []
for line in lines[:20]:
    onoff = line[1] == "n"
    m = map(int, re.findall(r'-?\d+', line))
    l = []
    for e in m:
        l.append(e)
    xmin = int(l[0])
    xmax = int(l[1])
    ymin = int(l[2])
    ymax = int(l[3])
    zmin = int(l[4])
    zmax = int(l[5])
    cubes.append(Cuboid(xmin,xmax,ymin,ymax,zmin,zmax,onoff))

r = 0
for i in range(-50,51):
    for j in range(-50,51):
        for z in range(-50,51):
            status = False
            for c in cubes:
                if isIn((i,j,z),c):
                    status = c.onoff
            if status:  
                r += 1
print(r)

