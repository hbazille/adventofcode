file1 = open('data/day14', 'r')
lines = file1.readlines()


def parse(line):
    t = line.split()
    i = 0
    l = []
    maxx, maxy = 0, 0
    while i < len(t):
        p = t[i].split(",")
        i += 2
        x = int(p[0])
        y = int(p[1])
        maxx = max(x, maxx)
        maxy = max(y, maxy)
        l.append((x, y))
    return l, maxx, maxy


def initgrid(n, m):
    grid = []
    for i in range(m):
        grid.append([])
        for j in range(n):
            grid[-1].append(".")
    return grid
        

def fillgrid(grid, linerock):
    i = 0
    while i < len(linerock) - 1:
        sx, sy = linerock[i]
        ex, ey = linerock[i + 1]
        if sx == ex:
            ylow = min(sy, ey)
            yup = max(sy, ey)
            for k in range(ylow, yup + 1):
                grid[k][sx] = "#"
        else:
            xlow = min(sx, ex)
            xup = max(sx, ex)
            for k in range(xlow, xup + 1):
                grid[sy][k] = "#"
        i += 1


def fillsand(grid, ps, LIMIT):
    psx, psy = ps
    while True:
        if psy > LIMIT:
            return 0
        if grid[psy + 1][psx] == ".":
            pass
        elif grid[psy + 1][psx - 1] == ".":
            psx -= 1
        elif grid[psy + 1][psx + 1] == ".":
            psx += 1
        else:
            grid[psy][psx] = "o"
            return 1
        psy += 1

rocks = []
maxx, maxy = 0, 0    
for line in lines[:-1]:
    rockline, x, y = parse(line)
    rocks.append(rockline)
    maxx = max(x, maxx)
    maxy = max(y, maxy)


grid = initgrid(maxx + 3, maxy + 5)
for linerock in rocks:
    fillgrid(grid, linerock)
    

count = 0
while fillsand(grid, (500, 0), maxy + 3) == 1:
    count += 1

print(count)

