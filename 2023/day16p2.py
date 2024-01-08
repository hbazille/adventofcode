
def change(di, dj, m):
    if m == ".":
        return [(di, dj)]
    if m == "/":
        return [(-dj, -di)]
    if m == "\\":
        return [(dj, di)]
    if m == "|":
        if di == 0:
            return [(-1, 0), (1, 0)]
        return [(di, dj)]
    if dj == 0:
        return [(0, -1), (0, 1)]
    return [(di, dj)]

def score(d, n):
    mask = [[0] * n for _ in range(n)]
    for (i, j, _, _) in d.keys():
        mask[i][j] = 1
    return sum(mask[i][j] for i in range(n) for j in range(n))

def move(t, e, n):
    d = {e : True}
    l = [e]
    while l != []:
        newl = []
        for (i, j, di, dj) in l:
            m = t[i][j]
            lij = change(di, dj,m)
            for (di, dj) in lij:
                i, j = i + di, j + dj
                if 0 <= i < n and 0 <= j < n and (i, j, di, dj) not in d.keys():
                    d[(i, j, di, dj)] = True
                    newl.append((i, j, di, dj))
        l = newl
    return score(d, n)   

def tryall(t):
    n = len(t)
    return max( \
        max(max(move(t, (i, 0, 0, 1), n), move(t, (i, n-1, 0, -1), n)) for i in range(n)), \
        max(max(move(t, (0, j, 1, 0), n), move(t, (n-1, j, -1, 0), n)) for j in range(n)))

if __name__ == "__main__":
    t = open('data/day16', 'r').readlines()
    n = len(t)
    for i in range(n):
        t[i] = t[i].strip()
    print(tryall(t))
    
