

def parseline(s):
    t = s.strip().split()
    return ("?".join(t[0] for _ in range(5))).split("."), list(map(lambda x : int(x), t[1].split(","))) * 5

def hashl(l):
    return ".".join(str(e) for e in l)
 
def dynprog(seq, l, d):
    hs, hl = hashl(seq), hashl(l)
    if (hs, hl) in d.keys():
        return d[(hs, hl)]
    if l == []:
        if any("#" in w for w in seq):
            return 0
        return 1
    if seq == []:
        return 0
    v = l[0]
    mystr = seq[0]
    if len(mystr) < v:
        if "#" in mystr:
            r = 0
        else:
            r = dynprog(seq[1:], l, d)
    elif len(mystr) == v:
        if "#" in mystr:
            r = dynprog(seq[1:], l[1:], d)
        else:
            r = dynprog(seq[1:], l[1:], d) + dynprog([seq[0][1:]] + seq[1:], l, d)
    elif mystr[0] == "#":
        if mystr[v] == "#":
            r = 0
        else:
            r = dynprog([seq[0][v+1:]] + seq[1:], l[1:], d)
    elif mystr[v] == "#":
        r = dynprog([seq[0][1:]] + seq[1:], l, d)
    else:
        r = dynprog([seq[0][v + 1:]] + seq[1:], l[1:], d) + dynprog([seq[0][1:]] + seq[1:], l, d)
    d[hs, hl] = r
    return r
    

  
if __name__ == "__main__":
    t = open('data/day12', 'r').readlines()
    print(sum(dynprog(*parseline(line), {}) for line in t))
        
