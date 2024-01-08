

def parseline(s):
    t = s.strip().split()
    return t[0].split("."), list(map(lambda x : int(x), t[1].split(",")))


def dynprog(seq, l):
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
            return 0
        return dynprog(seq[1:], l)
    if len(mystr) == v:
        if "#" in mystr:
            return dynprog(seq[1:], l[1:])
        return dynprog(seq[1:], l[1:]) + dynprog([seq[0][1:]] + seq[1:], l)
    if mystr[0] == "#":
        if mystr[v] == "#":
            return 0
        return dynprog([seq[0][v+1:]] + seq[1:], l[1:])
    if mystr[v] == "#":
        return dynprog([seq[0][1:]] + seq[1:], l)
    return dynprog([seq[0][v + 1:]] + seq[1:], l[1:]) + dynprog([seq[0][1:]] + seq[1:], l)
    
    
  
if __name__ == "__main__":
    t = open('data/day12', 'r').readlines()
    print(sum(dynprog(*parseline(line)) for line in t))
