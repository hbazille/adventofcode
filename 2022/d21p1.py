from functools import cmp_to_key

def parseline(line, d, val):
    t = line.split()
    resop = t[0][:-1]
    if len(t) == 4:
        d[resop] = [t[1], t[3]]
        val[resop] = (t[1], t[2], t[3])
    else:
        val[resop] = [int(t[1])]
        
def compare(m1, m2, d):
    if m1 in d[m2]:
        return -1
    elif m2 in d[m1]:
        return 1
    return 1

def fill(l, d):
    for e in l:
        i = 0
        while i < len(d[e]):
            v = d[e][i]
            d[e] += d[v]
            i += 1         

def findval(n, d, val, dop):
    if len(val[n]) == 1:
        return val[n][0]
    op1, op, op2 = val[n]
    vop1 = findval(op1, d, val, dop)
    vop2 = findval(op2, d, val, dop)
    v = dop[op](vop1, vop2)
    val[n] = [v]
    return v

if __name__ == '__main__':
    file = open('data/day21', 'r')
    lines = file.readlines()
    dop = {}
    for op in ["+", "-", "*"]:
        dop[op] = eval("lambda op1, op2: op1" + op + "op2")
    dop["/"] = (lambda op1, op2: op1 // op2)
    d, val = {}, {}
    for line in lines[:-1]:
        parseline(line, d, val)
    print(findval("root", d, val, dop))
    
