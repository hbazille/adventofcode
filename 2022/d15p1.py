file1 = open('data/day15', 'r')
lines = file1.readlines()

TARGET = 2000000

def parse(line):
    t = line.split()
    xs = int(t[2][2:-1])
    ys = int(t[3][2:-1])
    xb = int(t[-2][2:-1])
    yb = int(t[-1][2:])
    return((xs, ys), (xb, yb))
    
def manhattan(s, b):
    return abs(s[0] - b[0]) + abs(s[1] - b[1])

def saferange(s, d, TARGET):
    v = abs(s[1] - TARGET) 
    if  v > d:
        return None
    return (s[0] - (d-v), s[0] + (d-v))

def union(l, c):
    sc, ec = c
    r = []
    i = 0
    inc = False
    while i < len(l) and not inc:
        si, ei = l[i]
        if ei < sc - 1:
            r.append((si, ei))
        elif ec < si - 1:
            r.append((sc, ec))
            r.append((si, ei))
            inc = True
        else:
            sc = min(si,sc)
            ec = max(ei,ec)    
        i += 1
    if not inc:
        r.append((sc, ec))
    for j in range(i, len(l)):
        r.append(l[j])
    return r

def somme(lsafe):
    r = 0
    for l in lsafe:
        r += l[1] - l[0] + 1
    return r

def intersect(lsafe, beacons, TARGET):
    count = 0
    for b in beacons:
        bx, by = b
        if by == TARGET:
            for l in lsafe:
                if l[0] <= bx <= l[1]:
                    count += 1
    return count
    
lsafe = []
beacons = []
for line in lines[:-1]:
    s, b = parse(line)
    if b not in beacons:
        beacons.append(b)
    d = manhattan(s, b)
    sf = saferange(s, d, TARGET)
    if sf != None:
        lsafe = union(lsafe, sf)

print(somme(lsafe) - intersect(lsafe, beacons, TARGET))
