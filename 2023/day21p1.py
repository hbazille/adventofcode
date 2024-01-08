	

def next(t, i, j, dnext, n, m):
    for (di, dj) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m and t[ni][nj] != "#":
            dnext[(ni, nj)] = 1
            
            
def nextstep(t, d, n, m):
    dnext = {}
    for (i, j) in d.keys():
        next(t, i, j, dnext, n, m)
    return dnext
    
    
if __name__ == "__main__":
    t = open('data/day21', 'r').readlines()
    n = len(t)
    m = len(t[0]) - 1
    d = {(n // 2, m // 2) : 1}
    for _ in range(64):
        d = nextstep(t, d, n, m)
    print(len(d.keys()))
