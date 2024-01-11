file1 = open('data/exo15', 'r')
lines = file1.readlines()

def gen_mat(lines):
    M = []
    G = []
    i = 0
    for line in lines[:-1]:
        M.append([])
        G.append([])
        for c in line[:-1]:
            M[i].append(int(c))
            G[i].append(False)
        i += 1
    return M, G

mat, grid = gen_mat(lines)

def __sc_view(mat, i, j, di, dj):
    h = mat[i][j]
    k = 1
    while 0 <= i+k*di < len(mat) and 0 <= j+k*dj < len(mat[0]) and mat[i+k*di][j+k*dj] < h:
       k  += 1
    if 0 <= i+k*di < len(mat) and 0 <= j+k*dj < len(mat[0]):
        return k
    return k-1

def sc_view(mat, i, j):
    m = 1
    for (di, dj) in [(1,0), (0,1), (-1,0), (0,-1)]:
        m *= __sc_view(mat, i, j, di, dj)
    return m 

def pp(grid):
    for l in grid:
        for b in l:
            if b:
                print("1", end = "")
            else:
                print(" ", end = "")
        print()

biggest = 0

for i in range(1, len(mat) - 1):
    for j in range(1, len(mat) - 1):
        biggest = max(biggest, sc_view(mat, i, j))
     
print(biggest)
