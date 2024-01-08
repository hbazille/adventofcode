def moven(t, i, j):
    di = i - 1
    while di >= 0 and t[di][j] == ".":
        di -= 1
    di += 1
    t[i][j], t[di][j] = t[di][j], t[i][j]
  
def tiltn(t, n):
    for i in range(n):
        for j in range(n):
            if t[i][j] == "O":
                moven(t, i, j)

def buildt(t, n):
    r = []
    for i in range(n):
        r.append([])
        for j in range(n):
            r[i].append(t[i][j])
    return r

def loadt(t, n):
    return sum( ((n-i) * sum(1 for j in range(n) if t[i][j] == "O")) for i in range(n))
    
    

if __name__ == "__main__":
    t = open('data/day14', 'r').readlines()
    n = len(t)
    t = buildt(t, n)
    tiltn(t, n)
    print(loadt(t, n))
    
