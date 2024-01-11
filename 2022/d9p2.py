file1 = open('data/exo17', 'r')
lines = file1.readlines()

def nexthead(p, dp):
    p0 = p[0]
    p1 = p[1]
    if dp == "U":
        return (p0, p1+1)
    if dp == "D":
        return (p0, p1-1)
    if dp == "L":
        return (p0-1, p1)
    else:
        return (p0+1, p1)

def nexttail(ph, pd):
    difh = ph[0] - pd[0]
    difv = ph[1] - pd[1]
    if -1 <= difh <= 1 and -1 <= difv <= 1:
        return pd
    movh = 0
    if difh != 0:
        movh = difh // (abs(difh))
    movv = 0
    if difv != 0:
        movv = difv // (abs(difv))
    return (pd[0] + movh, pd[1] + movv)
    
p = []
for _ in range(10):
    p.append((0,0))

r = []
        
for line in lines[:-1]:
    l = line.split()
    for k in range(int(l[1])):
        p[0] = nexthead(p[0], l[0])
        for i in range(1, 10):
            p[i] = nexttail(p[i-1], p[i])
        r.append(p[9])

r.sort()
k = 1
for i in range(1, len(r)):
    if r[i-1] != r[i]:
        k += 1
print(k)
