


class Rating:
    def __init__ (self, x, m, a, s):
        self.x = x
        self.m = m
        self.a = a
        self.s = s
        
    def __str__(self):
        return str(self.x) + " m " + str(self.m) + " a " +  str(self.a) + " s " + str(self.s)
        
def parserating(l):
    t = l[1:-1].split(",")
    return Rating(int(t[0][2:]), int(t[1][2:]), int(t[2][2:]), int(t[3][2:]))

def makerule(l):
    if ":" not in l:
        return (lambda x : l)
    ic = l.index(":")
    dest = l[ic+1:]
    op = l[0:ic]
    return (lambda r : dest if eval("r." + op) else None)
    
def parserule(l, d):
    ib = l.index("{")
    name = l[:ib]
    rules = l[ib+1:-1]
    listrules = []
    for r in rules.split(","):
        listrules.append(makerule(r))
    d[name] = listrules

def score(r):
    return r.x + r.m + r.a + r.s
    
def run(r, d):
    s = "in"
    while s != "A" and s != "R":
        l = d[s]
        j = 0
        news = None
        while news == None:
            news = l[j](r)
            j += 1
        s = news
    if s == "A":
        return score(r)
    return 0
    
if __name__ == "__main__":
    d = {}
    t = open('data/day19', 'r').readlines()
    i, n = 0, len(t)
    while len(t[i]) > 2:
        parserule(t[i].strip(), d)
        i += 1
    i += 1
    s = 0
    while i < len(t):
        r = parserating(t[i].strip())
        s += run(r, d)
        i += 1
    print(s)
