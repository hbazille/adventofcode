
def move(l, val, pos):
    n = len(l) - 1
    l.pop(pos)
    newpos = (pos + val) % n
    l.insert(newpos, (val, True))
    
def fillcopy(l):
    copy = []
    for e, _ in l:
        copy.append(e)
    return copy
    
if __name__ == '__main__':
    
    file = open('data/day20', 'r')
    lines = file.readlines()
    l = []
    for line in lines[:-1]:
        l.append((int(line[:-1]),False))
    i = 0
    while i < len(l):
        v,f = l[i]
        if not f:
            move(l, v, i)
        else:
            i += 1
    copy = fillcopy(l)
    idx0 = copy.index(0)
    print(sum(copy[(idx0 + i*1000)%len(copy)] for i in range(1,4)))

