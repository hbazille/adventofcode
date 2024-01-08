
def parseline(s):
    return list(map(lambda x : int(x), s.split()))

def onlyz(l):
    return all(e == 0 for e in l)

def nextseq(l):
    return [(l[i+1] - l[i]) for i in range(len(l)-1)]
    
def getallseq(l):
    r = []
    while not onlyz(l):
        r.append(l[0])
        l = nextseq(l)
    return r
    
def extrapolate(r):
    i = len(r) - 1
    v = 0
    while i >= 0:
        v = r[i] - v
        i -= 1
    return v
    
if __name__ == "__main__":
    print(sum(extrapolate(getallseq(parseline(line))) for line in open('data/day9', 'r').readlines()))
