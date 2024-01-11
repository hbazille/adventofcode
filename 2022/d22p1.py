def pp(grid):
    for l in grid:
        print(l)
    print()

def firstlast(grid):
    limlines, limcols = [], []
    n, m = len(grid), len(grid[0])
    for i in range(n):
        j = 0
        while grid[i][j] == " ":
            j += 1
        jend = m - 1
        while grid[i][jend] == " ":
            jend -= 1
        limlines.append((j, jend))
    for j in range(m):
        i = 0 
        while grid[i][j] == " ":
            i += 1
        iend = n - 1
        while grid[iend][j] == " ":
            iend -= 1
        limcols.append((i, iend))
    return limlines, limcols
    
def nextfacing(cur, rot):
    l = ["R", "D", "L", "U"]
    if rot == "F":
        return cur
    move = 1 if rot == "R" else -1
    idx = l.index(cur)
    #print(cur, rot, move, l[(idx + move) % 4])
    return l[(idx + move) % 4]

def parsemove(l, i):
    k = 0
    while i < len(l) and "0" <= l[i] <= "9":
        k = k*10 + int(l[i])
        i += 1
    if i < len(l):
        return k, l[i], i+1    
    return k, "F", i+1    
        
    
            
def next(grid, p, dp, limlines, limcols):
    i, j = p
    newi, newj = i, j
    di, dj = dp
    limld, limlf = limlines[i]
    limcd, limcf = limcols[j]
    if di == 1 and limcf == i:
        newi = limcd
    elif di == -1 and limcd == i:
        newi = limcf
    elif dj == 1 and limlf == j:
        newj = limld
    elif dj == -1 and limld == j:
        newj = limlf
    else:
        newi = i + di
        newj = j + dj
    if grid[newi][newj] == ".":
        return newi, newj, True
    return i, j, False

def score(i, j, face):
    l = ["R", "D", "L", "U"]
    return 1000 * i + 4 * j + l.index(face)
            
if __name__ == '__main__':
    d = {"U" : (-1, 0), "R" : (0, 1), "D": (1,0), "L": (0,-1)}
    file = open('data/day22', 'r')
    lines = file.readlines()
    grid = []
    for line in lines[:-3]:
        l = line[:-1]
        l = l + (150 - len(l)) * " "
        grid.append(l)
    limlines, limcols = firstlast(grid)
    i, j = 0, limlines[0][0]
    face = "R"
    idx = 0
    listmoves = lines[-2][:-1]
    while idx < len(listmoves):
        length, rot, idx = parsemove(listmoves, idx)
        for _ in range(length):
            i, j, moved = next(grid, (i, j), d[face], limlines, limcols)
            if not moved:
                break
        face = nextfacing(face, rot)
    print(score(i+1, j+1, face))
    
    
    
    
    
    
