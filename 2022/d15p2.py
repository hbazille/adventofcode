
def parse(line):
    t = line.split()
    xs = int(t[2][2:-1])
    ys = int(t[3][2:-1])
    xb = int(t[-2][2:-1])
    yb = int(t[-1][2:])
    return((xs, ys), (xb, yb))
    
def manhattan(s, b):
    return abs(s[0] - b[0]) + abs(s[1] - b[1])

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


if __name__ == "__main__":
    file1 = open('data/exo29', 'r')
    lines = file1.readlines()

    sensors = []

    for line in lines[:-1]:
        s, b = parse(line)
        d = manhattan(s, b)
        sensors.append((s, d))

    K = 4000000
    for TARGET in range(0, K+1):
        lsafe = []
        for (s,d) in sensors:
            v = abs(s[1] - TARGET)
            if v <= d:
                lsafe = union(lsafe,(s[0] - (d-v), s[0] + (d-v)))
        if len(lsafe) > 1:
            print(TARGET + (lsafe[0][1]+1) * 4000000)
            break
