
class BinTree:
    def __init__(self, op, v1, v2):
        self.op = op
        self.v1 = v1
        self.v2 = v2

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
    if n == "humn":
        return BinTree("x", None, None), "st"
    if len(val[n]) == 1:
        return val[n][0], "int"
    op1, op, op2 = val[n]
    vop1, typ1 = findval(op1, d, val, dop)
    vop2, typ2 = findval(op2, d, val, dop)
    if n == "root":
        return vop1, vop2
    if typ1 == "st" or typ2 == "st":
        return BinTree(op, vop1, vop2), "st"
    v = dop[op](vop1, vop2)
    val[n] = [v]
    return v, "int"


def solve(lhs, rhs):
    if isinstance(rhs, BinTree):
        lhs, rhs = rhs, lhs
    if lhs.op == "x":
        return rhs
    if lhs.op == "+":
        if isinstance(lhs.v1, BinTree):
            return solve(lhs.v1, rhs - lhs.v2)
        else:
            return solve(lhs.v2, rhs - lhs.v1)
    if lhs.op == "-":
        if isinstance(lhs.v1, BinTree):
            return solve(lhs.v1, rhs + lhs.v2)
        else:
            return solve(lhs.v2, lhs.v1 - rhs)
    if lhs.op == "*":
        if isinstance(lhs.v1, BinTree):
            return solve(lhs.v1, rhs//lhs.v2)
        else:
            return solve(lhs.v2, rhs//lhs.v1)
    if lhs.op == "/":
        if isinstance(lhs.v1, BinTree):
            return solve(lhs.v1, rhs * lhs.v2)
        else:
            return solve(lhs.v2, lhs.v1 // rhs)
            
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
    lhs, rhs = findval("root", d, val, dop)
    print(solve(lhs, rhs))
