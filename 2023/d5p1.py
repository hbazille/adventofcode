    
def parsefirstline(s):
    return list(map(lambda x : int(x), s[s.index(":")+2:].strip().split()))
    
def parseotherlines(s):
    return tuple(map(lambda x : int(x), s.strip().split()))
    
def nextseed(t, l):
    n = len(l)
    i = 0
    while i < n:
        dest, src, rng = l[i]
        if t >= src and t < src + rng:
            return dest + t - src
        i += 1
    return t

if __name__ == "__main__":
    file1 = open('data/day5', 'r')
    lines = file1.readlines()
    n = len(lines)
    seeds = parsefirstline(lines[0])
    cv = []
    i = 3
    for types in range(7):
        cv.append([])
        while i < n and len(lines[i]) > 2:
            cv[types].append(parseotherlines(lines[i]))
            i += 1
        i += 2
    minloc = 100000000000000000
    for seed in seeds:
        for i in range(7):
            seed = nextseed(seed, cv[i])
        minloc = min(minloc, seed)
    print(minloc)
