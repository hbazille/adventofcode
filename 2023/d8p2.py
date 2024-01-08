import math
from functools import reduce

def parseline(s, d):
    key = s[0:3]
    d["L"][key] = s[7:10]
    d["R"][key] = s[12:15]
    return key

def howmany(seq, start, d):
    c, i, n = 0, 0, len(seq) - 1
    while start[-1] != "Z":
        start = d[seq[i]][start]
        c += 1
        i = (i + 1) % n
    return c

if __name__ == "__main__":
    t = open('data/day8', 'r').readlines()
    d = {"L" : {}, "R" : {}}
    l = [key for line in t[2:] if (key := parseline(line, d))[-1] == "A"]
    print(reduce(math.lcm, [howmany(t[0], e, d) for e in l], 1))
    
