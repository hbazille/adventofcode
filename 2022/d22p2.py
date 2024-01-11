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

            
def next(grid, p, face, limlines, limcols):
    d = {"U" : (-1, 0), "R" : (0, 1), "D": (1,0), "L": (0,-1)}
    i, j = p
    newi, newj = i, j
    di, dj = d[face]
    newface = face
    limld, limlf = limlines[i]
    limcd, limcf = limcols[j]
    if di == 1 and limcf == i:
        if j < 50:
            newi = 0
            newj = 100 + j
        elif j < 100:
            newface = "L"
            newi = 150 + j - 50
            newj = 49
        else:
            newface = "L"
            newi = 50 + j - 100
            newj = 99
    elif di == -1 and limcd == i:
        if j < 50:
            newface = "R"
            newi = 50 + j
            newj = 50
        elif j < 100:
            newface = "R"
            newi = 100 + j
            newj = 0
        else:
            newi = 199
            newj = j - 100
    elif dj == 1 and limlf == j:
        if i < 50:
            newface = "L"
            newi = 149 - i
            newj = 99
        elif i < 100:
            newface = "U"
            newi = 49
            newj = i + 50
        elif i < 150:
            newface = "L"
            newi = 149 - i
            newj = 149
        else:
            newface = "U"
            newi = 149
            newj = i - 100
    elif dj == -1 and limld == j:
        if i < 50:
            newface = "R"
            newi = 149 - i
            newj = 0
        elif i < 100:
            newface = "D"
            newi = 100
            newj = i - 50
        elif i < 150:
            newface = "R"
            newi = 149 - i
            newj = 50
        else:
            newface = "D"
            newi = 0
            newj = i - 100
    else:
        newi = i + di
        newj = j + dj
    if grid[newi][newj] == ".":
        return newi, newj, newface, True
    return i, j, face, False

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
            i, j, face, moved = next(grid, (i, j), face, limlines, limcols)
            if not moved:
                break
        face = nextfacing(face, rot)
    print(score(i+1, j+1, face))
    
    
    
    
    
    
