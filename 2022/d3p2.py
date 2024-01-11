file1 = open('data/exo5', 'r')
lines = file1.readlines()


def prio(c):
    if 'a' <= c <= 'z':
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 2day3


def same(l1, l2, l3):
    i, j, k = 0, 0, 0
    while i < len(l1) and j < len(l2) and k < len(l3):
        ci, cj, ck = l1[i], l2[j], l3[k]
        if ci == cj == ck:
            return ci
        elif ci <= cj and ci <= ck:
            i += 1
        elif cj <= ci and cj <= ck:
            j += 1
        else:
            k += 1
  
  
sc = 0
i = 0
while i < len(lines) - 3:
    l1 = []
    l2 = []
    l3 = []
    for e in lines[i][:-1]:
        l1.append(e)
    for e in lines[i+1][:-1]:
        l2.append(e)
    for e in lines[i+2][:-1]:
        l3.append(e)
    l1.sort()
    l2.sort()
    l3.sort()
    p = same(l1, l2, l3)
    sc += prio(p)
    i += 3
print(sc)   
