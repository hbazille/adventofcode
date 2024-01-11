file1 = open('data/day8', 'r')
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

i = 0
while i < len(mat):
    j = 0
    #while j < len(mat[0]) and mat[i][j] == 0:
    #    j += 1
    if j < len(mat[0]):
        grid[i][j] = True
        biggest = mat[i][j]
    j += 1
    while j < len(mat[0]) and mat[i][j] < 9:
        if mat[i][j] > biggest:
            grid[i][j] = True
            biggest = mat[i][j]
        j += 1
    if j < len(mat[0]):
        grid[i][j] = True
    i += 1

i = 0
while i < len(mat):
    j = 0
    #while j < len(mat[0]) and mat[i][-1-j] == 0:
    #    j += 1
    if j < len(mat[0]):
        grid[i][-1-j] = True
        biggest = mat[i][-1-j]
    j += 1
    while j < len(mat[0]) and mat[i][-1-j] < 9:
        if mat[i][-1-j] > biggest:
            grid[i][-1-j] = True
            biggest = mat[i][-1-j]
        j += 1
    if j < len(mat[0]):
        grid[i][-1-j] = True
    i += 1

j = 0
while j < len(mat[0]):
    i = 0
    #while i < len(mat) and mat[i][j] == 0:
    #    i += 1
    if i < len(mat):
        grid[i][j] = True
        biggest = mat[i][j]
    i += 1
    while i < len(mat) and mat[i][j] < 9:
        if mat[i][j] > biggest:
            grid[i][j] = True
            biggest = mat[i][j]
        i += 1
    if i < len(mat):
        grid[i][j] = True
    j += 1
    
    
j = 0
while j < len(mat[0]):
    i = 0
    #while i < len(mat) and mat[-1-i][j] == 0:
    #    i += 1
    if i < len(mat):
        grid[-1-i][j] = True
        biggest = mat[-1-i][j]
    i += 1
    while i < len(mat) and mat[-1-i][j] < 9:
        if mat[-1-i][j] > biggest:
            grid[-1-i][j] = True
            biggest = mat[-1-i][j]
        i += 1
    if i < len(mat):
        grid[-1-i][j] = True
    j += 1

def count1(grid):
    r = 0
    for l in grid:
        for c in l:
            r += c
    return r

def pp(grid):
    for l in grid:
        for b in l:
            if b:
                print("1", end = "")
            else:
                print(" ", end = "")
        print()
print(count1(grid))
