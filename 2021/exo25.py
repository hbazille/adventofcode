import re

l = []
file1 = open('data/exo25', 'r')
lines = file1.readlines()

#lines = ["start-A\n","start-b\n","A-c\n","A-b\n","b-d\n","A-end\n","b-end\n",""]

points = []

def addpoint(l,p):
    if p not in l:
        l.append(p)

def foldLeft(points,x):
    res = []
    for p in points:
        if p[0]>x:
            addpoint(res,(2*x-p[0],p[1]))
        elif p[0]<x:
            addpoint(res,p)
    return res

def foldUp(points,y):
    res = []
    for p in points:
        if p[1]>y:
            addpoint(res,(p[0],2*y-p[1]))
        elif p[1]<y:
            addpoint(res,p)
    return res

cptline = 0
while len(lines[cptline]) > 1:
    line = lines[cptline]
    l = line[:-1].split(",")
    points.append((int(l[0]),int(l[1])))
    cptline += 1

points = foldLeft(points,655)
print(len(points))
