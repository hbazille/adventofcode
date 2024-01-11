file1 = open('data/day3', 'r')
lines = file1.readlines()


def prio(c):
    if 'a' <= c <= 'z':
        return ord(c) - ord('a') + 1
    else:
        return ord(c) - ord('A') + 27


def same(l1, l2):
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] == l2[j]:
            return l1[i]
        elif l1[i] < l2[j]:
            i += 1
        else:
            j += 1
  
  
sc = 0
i = 0
while i < len(lines) - 1:
    l1 = []
    l2 = []
    line = lines[i]
    m = (len(line) - 1) // 2
    for e in line[:m]:
        l1.append(e)
    for e in line[m:-1]:
        l2.append(e)
    l1.sort()
    l2.sort()
    p = same(l1, l2)
    sc += prio(p)
    i += 1
print(sc)   
