import re
import itertools

l = []
file1 = open('data/exo47', 'r')
lines = file1.readlines()


nb = [9,8,7,6,5,4,3,2,1]

criteria = [0,0,0,13,0,0,7,0,9,0,17,9,8,8,0]

criteriamin = [0,0,0,14,0,0,8,0,10,0,18,10,9,9,0]
criteriamax = [0,0,0,22,0,0,16,0,18,0,25,18,17,17,0]


def test(listnumbers,k):
    global lines
    x,y,z,w = 0,0,0,0
    i = 0
    while i < k:
        w = listnumbers[i]
        elem1 = int(lines[18*i+5][:-1].split()[2])
        x = z%26 + elem1
        elemdiv = int(lines[18*i+4][:-1].split()[2])
        z = z//elemdiv
        elem2 = int(lines[18*i+15][:-1].split()[2])
        if w != x:
            z = 26*z + w + elem2
        i += 1 
        #print(elemdiv,elem1,elem2)
    ztmp = z%26
    #print(z)
    if criteria[k] == 0:
        return z,[9,8,7,6,5,4,3,2,1]
    elif (ztmp > criteriamax[k] or ztmp < criteriamin[k]):
        return z,[]
    else: 
        return z,[ztmp-criteria[k]]
    

dico = {}
listall = [[9],[8],[7],[6],[5],[4],[3],[2],[1]]

test([9,1,8,9,7,3,9,9,4,9,8,9,9,5],14)
test([5,1,1,2,1,1,7,6,1,2,1,3,9,1],14)
for e in [5,1,1,2,1,1,7,6,1,2,1,3,9,1]:
    print(e,end="")
print()

"""
for i in range(14):
    print(i,len(listall))
    dico = {}
    """ """
    newl = []
    for l in listall:
        for n in nb:
            newl.append(l+[n])
    listall = newl
    """ """
    final = []
    for l in listall:
        z,follow = test(l,i+1)
        if follow != []:
            if z not in dico.keys():
                dico[z] = l
                for n in follow:
                    final.append(l+[n])
    listall = final

mini = 1000000000
minl = []
t = 0
for k in dico.keys():
    t += 1
    if k < mini:
        mini = k
        minl = dico[k]

print(mini,minl,t)
"""
