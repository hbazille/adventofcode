import re

l = []
file1 = open('data/day12', 'r')
lines = file1.readlines()

#lines = ["start-A","start-b","A-c","A-b","b-d","A-end","b-end"]

r = 0
vertices = []
edges = {}

for line in lines[:-1]:
    l = line[:-1].split("-")
    for s in l:
        if s not in vertices:
            vertices.append(s)
            edges[s] = []
    edges[l[0]].append(l[1])
    edges[l[1]].append(l[0])


def nbpaths(vertices,edges,s,chain):
    global r 
    for adj in edges[s]:
        if adj == "end":
            r += 1
        elif adj < "a":
            nbpaths(vertices,edges,adj,chain)
        elif not adj in chain:
            nbpaths(vertices,edges,adj,chain+[adj])

nbpaths(vertices,edges,"start",["start"])
print(r)
