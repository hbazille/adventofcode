

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
    
    
def tryfull(t, i, j, n, m, k = 312):
    d = {(i, j) : 1}
    for _ in range(k):
        d = nextstep(t, d, n, m)
    nk = len(d.keys())
    d = nextstep(t, d, n, m)
    return nk, len(d.keys())
    

if __name__ == "__main__":
    t = open('data/day21', 'r').readlines()
    n = len(t)
    m = len(t[0]) - 1
    (pair, impair) = tryfull(t, n//2, m//2, n, m, 132)
    middle65 = tryfull(t, n // 2, m // 2, n, m, 65)[0]
    corner = tryfull(t, 0, 0, n, m, 64)[0] + tryfull(t, n-1, 0, n, m, 64)[0] + tryfull(t, 0, m-1, n, m, 64)[0] + tryfull(t, n-1, m-1, n, m, 64)[0]
    mid = tryfull(t, n//2, 0, n, m, 130)[0] + tryfull(t, n//2, m-1, n, m, 130)[0] + tryfull(t, 0, m//2, n, m, 130)[0] + tryfull(t, n-1, m//2, n, m, 130)[0]
    middle196 = pair + corner + mid
    bigcorner = tryfull(t, 0, 0, n, m, 195)[0] + tryfull(t, n-1, 0, n, m, 195)[0] + tryfull(t, 0, m-1, n, m, 195)[0] + tryfull(t, n-1, m-1, n, m, 195)[0]
    middle327 = impair + 4 * pair + mid + 2*corner + bigcorner
    k = 26501300 // 131
    c = middle65
    a = (middle327 - 2 * middle196 + c) // 2
    b = middle196 - c - a
    print(a * k * k + b * k + c)
    
