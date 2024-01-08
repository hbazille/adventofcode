from functools import cmp_to_key

def parseline(s):
    return s.strip().split()
    
def scorecard(t):
    return "J23456789TQKA".index(t)
    
def kind(s):
    s1 = ""
    nbj = 0
    for c in s:
        if c == "J":
            nbj += 1
        else:
            s1 += c
    t = [e for e in s1]
    t.sort()
    i, l = 0, []
    while i < len(s1) - 1:
        c = 0
        while i < len(s1) - 1 and t[i] == t[i+1]:
             c += 1
             i += 1
        i += 1
        l.append(c)
    l.sort()
    if l == []:
        l = [4]
    else:
        l[-1] += nbj
    if l[-1] == 4:
        return 6
    elif l[-1] == 3:
        return 5
    elif l[-1] == 2:
        if l[-2] == 1:
            return 4
        return 3
    elif l[-1] == 1:
        if l[-2] == 1:
            return 2
        return 1
    return 0        

def compare(w1, w2):
    s1, s2 = w1[0], w2[0]
    sc1 = kind(s1)
    sc2 = kind(s2)
    if sc1 < sc2:
        return -1
    elif sc1 > sc2:
        return 1
    else:
        i = 0
        while i < 5 and s1[i] == s2[i]:
            i += 1
        if i == 5:
            return 0
        else:
            return scorecard(s1[i]) - scorecard(s2[i])

if __name__ == "__main__":
    file1 = open('data/day7', 'r')
    lines = file1.readlines()
    t = [parseline(l) for l in lines]
    t.sort(key=cmp_to_key(compare))
    s, i, n = 0, 0, len(t)
    while i < n:
        s += (i + 1) * int(t[i][1])
        i += 1
    print(s)
