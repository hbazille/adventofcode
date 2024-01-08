
def parseline(s):
    return list(map(lambda x : int(x), s.split()))

def onlyz(l):
    return all(e == 0 for e in l)

def nextseq(l):
    return [(l[i+1] - l[i]) for i in range(len(l)-1)]
    
def getallseq(l):
    r = 0
    while not onlyz(l):
        r += l[-1]
        l = nextseq(l)
    return r
    
if __name__ == "__main__":
    print(sum(getallseq(parseline(line)) for line in open('data/day9', 'r').readlines()))
