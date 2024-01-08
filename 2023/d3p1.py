
import numpy as np

def buildarray(t, T, n, m):
    for i in range(n):
        for j in range(m):
            T[i, j] = t[i][j]

def subarray(T, i, j, mi, mj):
    mini = max(i - 1, 0)
    maxi = min(i + 2, mi)
    minj = max(j - 1, 0)
    maxj = min(j + 2, mj)
    return T[mini : maxi, minj : maxj]

def checkaround(T, values):
    return any(np.in1d(values, T))
     
def readl(T, i, n, m, nb, values):
    s = 0
    j = 0
    while j < m:
        while j < m and T[i, j] not in nb:
            j += 1
        if j == m:
            break
        c = int(T[i, j])
        b = checkaround(subarray(T, i, j, n, m), values)
        j += 1
        while j < m and T[i, j] in nb:
            b = b or checkaround(subarray(T, i, j, n, m), values)
            c = 10 * c + int(T[i, j])
            j += 1
        if b:
            s += c
    return s

def readarray(T, n, m, nb, values):
    return sum(readl(T, i, n, m, nb, values) for i in range(n))

if __name__ == "__main__":
    file1 = open('data/day3', 'r')
    t = file1.readlines()
    n = len(t)
    m = len(t[0]) - 1
    values = []
    for i in range(n):
        for j in range(m):
            v = t[i][j]
            if v not in ".0123456789" and v not in values:
                values.append(v)
    values = np.array(values, dtype='S1')
    nb = np.array(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], dtype='S1')
    T = np.zeros((n, m), dtype='S1')
    buildarray(t, T, n, m)
    print(readarray(T, n, m, nb, values))
        
