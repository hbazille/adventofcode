

def interinf(r, v):
    lb, ub = r
    if v <= lb:
        return None, (r)
    if v > ub:
        return r, None
    return (lb, v - 1), (v, ub)
        
def intersup(r, v):
    lb, ub = r
    if v >= ub:
        return r, None
    if v < lb:
        return None, r
    return (v + 1, ub), (lb, v)

def makerule(l):
    if ":" not in l:
        return l
    ic = l.index(":")
    return (l[1], l[0], int(l[2:ic]), l[ic+1:])
    
def parserule(l, d):
    ib = l.index("{")
    listrules = []
    for r in l[ib+1:-1].split(","):
        listrules.append(makerule(r))
    d[l[:ib]] = listrules

def score(r):
    xmin, xmax = r[0]
    smin, smax = r[1]
    mmin, mmax = r[2]
    amin, amax = r[3]
    return (xmax - xmin + 1) * (smax - smin + 1) * (mmax - mmin + 1) * (amax - amin + 1)


def lettoidx(let):
    return "xmas".index(let)

    
def optoop(op):
    if op == "<":
        return interinf
    return intersup


def run(r, d):
    stack = [(r, "in")]
    res = 0
    while stack != []:
        r, s = stack.pop()
        if s == "A":
            res += score(r)
            continue
        elif s == "R":
            continue
        l = d[s]
        j = 0
        nl = len(l)
        while j < nl - 1:
            op, let, target, dest = l[j]
            idx = lettoidx(let)
            op = optoop(op)
            acc, ref = op(r[idx], target)
            newr = []
            if acc != None:             
                for i in range(4):
                    if i == idx:
                        newr.append(acc)
                    else:
                        newr.append(r[i])
                stack.append((newr, dest))
            if ref != None:
                r[idx] = ref
            else:
                break
            j += 1 
        if j == nl - 1:
            stack.append((r, l[j]))
    return res
    

if __name__ == "__main__":
    d = {}
    t = open('data/day19', 'r').readlines()
    i, n = 0, len(t)
    while len(t[i]) > 2:
        parserule(t[i].strip(), d)
        i += 1
    print(run([(1, 4000), (1, 4000), (1, 4000), (1, 4000)], d))
