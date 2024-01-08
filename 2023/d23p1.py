import sys
sys.setrecursionlimit(10000)
   

def dfs(t, d):
    n = len(t)
    M = [([None] * n) for _ in range(n)] 
    def rec(t, i, j, n):
        if i == n - 1 and j == n - 2:
            M[i][j] = 0
            return 0
        M[i][j] = -1
        maxi = -1
        for (di, dj) in d[t[i][j]]: 
            ni, nj = i + di, j + dj
            v = t[ni][nj]
            if 0 <= ni < n and 0 <= nj < n:
                wantogo = True
                if (v in "<>^v" and d[v][0] != (di, dj)):
                    wantogo = False 
                if M[ni][nj] == None and wantogo:
                    rec(t, ni, nj, n)
                if wantogo:
                    maxi = max(maxi, M[ni][nj])
        M[i][j] = 1 + maxi
    rec(t, 0, 1, n)
    return M[0][1] 
    
                 
if __name__ == "__main__":
    l = []
    d = {"#" : [], "." : [(-1, 0), (0, -1), (0, 1), (1, 0)], ">" : [(0, 1)], "^" : [(-1, 0)], "<" : [(0, -1)], "v" : [(1, 0)]}
    t = open('data/day23', 'r').readlines()
    print(dfs(t, d))
    
