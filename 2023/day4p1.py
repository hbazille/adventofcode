
def common(l1, l2):
    l1.sort()
    l2.sort()
    i, j = 0, 0
    s = 0
    n, m = len(l1), len(l2)
    while i < n and j < m:
        v1, v2 = l1[i], l2[j]
        i += v1 <= v2
        j += v1 >= v2
        s += v1 == v2
    if s == 0:
        return 0
    return int(2**(s-1))
    
def parseline(s):
    return list(map(lambda s : list(map(lambda x : int(x), s)), list(w.strip().split() for w in s[s.index(":")+2:].split("|"))))

if __name__ == "__main__":
    file1 = open('data/day4', 'r')
    s = 0
    for line in file1:
        l = parseline(line)
        s += common(l[0], l[1])
    print(s)
