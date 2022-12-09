import re

l = []
file1 = open('data/exo23', 'r')
lines = file1.readlines()

#lines = ["start-A\n","start-b\n","A-c\n","A-b\n","b-d\n","A-end\n","b-end\n",""]

r = 0
vertices = []
edges = {}


for line in lines[:-1]:
    l = line[:-1].split("-")
    for s in l:
        if s not in vertices:
            vertices.append(s)
            edges[s] = []
    if l[1] != "start":
        edges[l[0]].append(l[1])
    if l[0] != "start":
        edges[l[1]].append(l[0])

dico = {}
for v in vertices:
    if v>="a":
        dico[v] = 0

def nocc(l,c):
    r = 0
    for e in l:
        r += (e==c)
    return r

def nbpaths(vertices,edges,s,dico,twice):
    global r 
    for adj in edges[s]:
        if adj == "end":
            r += 1
        elif adj < "a":
            nbpaths(vertices,edges,adj,dico,twice)
        elif adj != "start":
            v = dico[adj] 
            if v == 0:
                dico[adj] += 1
                nbpaths(vertices,edges,adj,dico,twice)
                dico[adj] -= 1
            elif v == 1 and not twice: 
                dico[adj] += 1
                nbpaths(vertices,edges,adj,dico,True)
                dico[adj] -= 1

nbpaths(vertices,edges,"start",dico,False)
print(r)
