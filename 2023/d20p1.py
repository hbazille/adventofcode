from utils.queue import Queue

class FlipFlop:
    def __init__(self, dest):
        self.state = 0
        self.dest = dest
    
    def receive(self, inp, sig):
        if sig == 1:
            return None
        self.state = 1 - self.state
        return self.state, self.dest
    
    def send(self):
        return self.state, dest

class Conjunction:
    def __init__(self, dest):
        self.states = {}
        self.dest = dest
    
    def addwatch(self, inp):
        self.states[inp] = 0
        
    def receive(self, inp, val):
        self.states[inp] = val
        sig = -1
        if all(self.states[k] == 1 for k in self.states.keys()):
            return 0, self.dest
        return 1, self.dest
        
    
def firstparse(s, dc):
    s = s.split("->")
    name = s[0].strip()
    if name[0] == "b":
        name = "%" + name
    dc[name[1:]] = (name[0] == "&")

def filter(dc, l):
    newl = []
    for e in l:
        if e in dc.keys():
            newl.append(e)
    return newl

def parseinput(s, d, lc, dc):
    s = s.split("->")
    name = s[0].strip()
    if name[0] == "b":
        name = "%" + name
    dest = s[1].split(",")
    for i in range(len(dest)):
        dest[i] = dest[i].strip()
    if name[0] == "%":
        name = name[1:]
        d[name] = FlipFlop(dest)
        for dst in dest:
            if dst in dc.keys() and dc[dst]:
                lc.append((dst, name))
    else:
        name = name[1:]
        d[name] = Conjunction(dest)
        for dst in dest:
            if dst in dc.keys() and dc[dst]:
                lc.append((dst, name))


def fillconj(d, lc):
    for i, j in lc:
        d[i].states[j] = 0

    
def run(d):
    q = Queue()
    dest = d["broadcaster"].dest
    lows, highs = 1 + len(dest), 0
    for dst in dest:
        q.enqueue((dst, 0, "broadcaster"))
    while not q.isempty():
        dst, sig, src = q.dequeue()
        r = d[dst].receive(src, sig)
        if r == None:
            continue
        newsig, newdest = r
        #print(dst, newsig, newdest)
        if newsig == 0:
            lows += len(newdest)
        else:
            highs += len(newdest)
        for ndst in newdest:
            if ndst in d.keys():
                q.enqueue((ndst, newsig, dst))
    return lows, highs
    
    
if __name__ == "__main__":
    d, dc, lc = {}, {}, []
    t = open('data/day20', 'r').readlines()
    for s in t:
        firstparse(s, dc)
    for s in t:
        parseinput(s, d, lc, dc)
    fillconj(d, lc)
    l, h = 0, 0
    for _ in range(1000):
        lr, hr = run(d)
        l += lr
        h += hr
    print(l * h)
