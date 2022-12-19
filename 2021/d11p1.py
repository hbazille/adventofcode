import re

l = []
file1 = open('data/day11', 'r')
lines = file1.readlines()

r = 0
data = []

for line in lines:
    l = line.split()
    ln = []
    for c in l[0]:
        ln.append(int(c))
    data.append(ln)
flash = 0

def pp(data):
    for l in data:
        for e in l:
            print(e,end=" ")
        print()
    print()


def add1(data,i,j):
    for i1 in range(i-1,i+2):
        if i1>=0 and i1 < len(data):
            for j1 in range(j-1,j+2):
                if j1 >= 0 and j1<len(data[0]):
                    data[i1][j1] += 1

def step(data):
    global flash
    isFlash = True
    flashes = [[False]*10 for i in range(10)]
    for i in range(10):
        for j in range(10):
            data[i][j] += 1
    while isFlash:
        isFlash = False
        for i in range(10):
            for j in range(10):
                if not flashes[i][j] and data[i][j] > 9:
                    flashes[i][j] = True
                    flash += 1
                    isFlash = True
                    add1(data,i,j)
    for i in range(10):
        for j in range(10):
            if flashes[i][j]:
                data[i][j] = 0
for i in range(100):
    step(data)  
#pp(data)
print(flash)
