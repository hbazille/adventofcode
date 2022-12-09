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

def splitsegment(p1,p2):
    mini1,maxi1 = p1
    mini2,maxi2 = p2
    


def split(P1,P2):
    # splits P1 in parts that are not in P2 
    lx = []
    ly = []
    lz = []
    if P1.xmax < P2.xmin or P1.xmin > P2.xmax or P1.ymax < P2.ymin or P1.ymin > P2.ymax or P1.zmax < P2.zmin or P1.zmin > P2.zmax:
    # no intersection
        return [P1]
    else:
        pass    

def isIn(p,C):
    return p[0] >= C.xmin and p[0] <= C.xmax and p[1] >= C.ymin and p[1] <= C.ymax and p[2] >= C.zmin and p[2] <= C.zmax


#current is off:
#   take all and keep splits wrt current
#current is on:
#   split current wrt all and keep

cubes = []
for line in lines[:-1]:
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

kept = []
for c in cubes:
    newkept = []
    for c2 in kept:
        xmin = max(c.xmin,c2.xmin)
        xmax = min(c.xmax,c2.xmax)
        ymin = max(c.ymin,c2.ymin)
        ymax = min(c.ymax,c2.ymax)
        zmin = max(c.zmin,c2.zmin)
        zmax = min(c.zmax,c2.zmax)
        if xmin>xmax or ymin>ymax or zmin>zmax:
            pass
        else:
            newkept.append(Cuboid(xmin,xmax,ymin,ymax,zmin,zmax,not c2.onoff))
    kept += newkept
    if c.onoff:
        kept.append(c)


r = 0
for c in kept:
    if c.onoff:
        r += (c.xmax-c.xmin+1)*(c.ymax-c.ymin+1)*(c.zmax-c.zmin+1)
    else:
        r -= (c.xmax-c.xmin+1)*(c.ymax-c.ymin+1)*(c.zmax-c.zmin+1)

print(len(kept))        
print(r)
