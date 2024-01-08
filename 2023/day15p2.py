
def hashia(s):
    r = 0
    for i in range(len(s)):
        if s[i] in "-=":
            return r, i
        r = ((r + ord(s[i])) * 17) % 256

def remove(box, b):
    i = 0 
    while i < len(box) and box[i][0] != b:
        i += 1
    if i < len(box):
        box.pop(i)
        
def add(box, b, sc):
    i = 0 
    while i < len(box) and box[i][0] != b:
        i += 1
    if i < len(box):
        box[i] = (b, sc)
    else:
        box.append((b, sc))

def filllist(t, l):
    for s in t:
        sc, i = hashia(s)
        if s[i] == "-":
            remove(l[sc], s[:i])
        else:
            add(l[sc], s[:i], s[i+1:])

def score(l):
    return sum((i + 1) * (j + 1) * int(l[i][j][1]) for i in range(len(l)) for j in range(len(l[i])))
            
if __name__ == "__main__":
    t = open('data/day15', 'r').readlines()[0].strip().split(",")
    l = [[] for _ in range(256)]
    filllist(t, l)
    print(score(l))
    
