
import numpy as np

def buildarray(t, T, n, m):
    for i in range(n):
        for j in range(m):
            T[i, j] = t[i][j]


def getnumber(T, nb, i, j, n, m):
    c = 0
    while j >= 0 and T[i, j] in nb:
        j -= 1
    j += 1
    while j < m and T[i, j] in nb:
            c = 10*c + int(T[i, j])
            j += 1
    return c

def checkaroundstar(T, nb, i, j, n, m):
    total = 0
    s = 1
    found = 0
    # stars are never on the edge
    no_cc = [(i-1, j-1), (i, j-1), (i, j+1), (i+1, j-1)]
    cc = [(i-1, j), (i-1, j+1), (i+1, j), (i+1, j+1)]
    for (ci, cj) in no_cc:
        if T[(ci, cj)] in nb:
            found += 1
            s *= getnumber(T, nb, ci, cj, n, m)
    for (ci, cj) in cc:
        if T[ci, cj] in nb and T[ci, cj-1] not in nb:
            found += 1
            s *= getnumber(T, nb, ci, cj, n, m)
    if found == 2:
        return s
    return 0
     
     
def readl(T, i, n, m, nb, values):
    s = 0
    j = 0
    while j < m:
        while j < m and T[i, j] not in values:
            j += 1
        if j == m:
            break
        s += checkaroundstar(T, nb, i, j, n, m)
        j += 1
    return s

def readarray(T, n, m, nb, values):
    return sum(readl(T, i, n, m, nb, values) for i in range(n))

if __name__ == "__main__":
    file1 = open('data/day3', 'r')
    t = file1.readlines()
    n = len(t)
    m = len(t[0]) - 1
    values = np.array(["*"], dtype='S1')
    nb = np.array(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], dtype='S1')
    T = np.zeros((n, m), dtype='S1')
    buildarray(t, T, n, m)
    print(readarray(T, n, m, nb, values))
        
