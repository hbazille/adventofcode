import sys
sys.setrecursionlimit(10000)

from utils import graph


def dfs(G):
    n = G.order
    M = [False] * n
    def rec(G, i, c):
        if i == 1:
            return c
        M[i] = c
        maxi = 0
        for j in G.adjlists[i]: 
            if not M[j]:
                maxi = max(maxi, rec(G, j, c + G.costs[(i, j)]))
        M[i] = False
        return maxi
    return rec(G, 0, 0)

def isinter(t, i, j, n):
    c = 0
    for (di, dj) in [(-1, 0), (0, -1), (0, 1), (1, 0)]: 
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < n and t[ni][nj] != "#":
            c += 1
    return c > 2

def buildgraph(t):
    n = len(t)
    l = [(0, 1), (n-1, n-2)]
    a = []
    M = [([False] * n) for _ in range(n)] 
    def rec(t, i, j, n):
        if isinter(t, i, j, n):
            l.append((i, j))
        M[i][j] = True
        for (di, dj) in [(-1, 0), (0, -1), (0, 1), (1, 0)]: 
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and t[ni][nj] != "#" and not M[ni][nj]:
                rec(t, ni, nj, n)
    rec(t, 0, 1, n)
    m = len(l)
    G = graph.Graph(m, False, True)
    def rec2(t, i, j, n, target, M, c):
        M[i][j] = True
        for (di, dj) in [(-1, 0), (0, -1), (0, 1), (1, 0)]: 
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n and t[ni][nj] != "#" and not M[ni][nj]:
                if isinter(t, ni, nj, n):
                    if (ni, nj) == target:
                        return c + 1
                    return None
                d = rec2(t, ni, nj, n, target, M, c + 1)
                if d != None:
                    return d                    
    for i in range(m - 1):
        si, sj = l[i]
        for j in range(i+1, m):
            M = [([False] * n) for _ in range(n)] 
            d = rec2(t, si, sj, n, l[j], M, 0)
            if d != None:
                G.addedge(i, j, d)
    return G 
       
if __name__ == "__main__":
    l = []
    t = open('data/day23', 'r').readlines()
    G = buildgraph(t)
    print(dfs(G))
