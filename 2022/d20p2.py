

def move(l, val, pos):
    n = len(l) - 1
    v = l.pop(pos)
    newpos = (pos + val) % n
    l.insert(newpos, v)
    
    
def fillcopy(l):
    copy = []
    for e, _ in l:
        copy.append(e)
    return copy
    
if __name__ == '__main__':
    file = open('data/day20', 'r')
    lines = file.readlines()
    l = []
    order = []
    i = 0
    for line in lines[:-1]:
        v = int(line[:-1])
        l.append((811589153*v, i))
        order.append((811589153*v,i))
        i += 1
    for j in range(10):
        i = 0
        for c in order:
            idx = l.index(c)
            v = l[idx][0]
            move(l, v, idx)
            
    copy = fillcopy(l)
    idx0 = copy.index(0)
    print(sum(copy[(idx0 + i*1000)%len(copy)] for i in range(1,4)))
    
