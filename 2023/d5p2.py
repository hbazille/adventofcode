
def parsefirstline(s):
    l = list(map(lambda x : int(x), s[s.index(":")+2:].strip().split()))
    return [(l[i], l[i+1]) for i in range(0, len(l), 2)]
        
def parseotherlines(s):
    return list(map(lambda x : int(x), s.strip().split()))
    
def nextseed(t, l):
    n = len(l)
    i = 0
    s, r = t
    if r == 0:
        return []
    while i < n:
        dest, src, rng = l[i]
        if s >= src and s < src + rng:
            if r + s <= rng + src:
                return [(dest + s - src, r)]
            else:
                newr = rng + src - s
                res = [(dest + s - src, newr)]
                res += nextseed((s + newr, r - newr), l)
                return res
        elif s < src and s + r > src and s + r <= src + rng:
            newr = r + s - src
            res = [(src, newr)]
            res += nextseed((s, r - newr), l)
            return res
        elif s < src and s + r > src + rng:
            res = [(src, rng)]
            newr1 = src - s
            res += nextseed((s, newr1), l)
            newr2 = src + rng - s
            res += nextseed((s + newr2, r - newr2), l)
            return res
        i += 1
    return [t]

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
    for i in range(7):
        news = []
        for seed in seeds:
            news += nextseed(seed, cv[i])
        seeds = news
    print(min(seed[0] for seed in seeds))
