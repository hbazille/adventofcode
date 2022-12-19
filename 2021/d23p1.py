import re

"""
l = []
file1 = open('data/day23', 'r')
lines = file1.readlines()
"""

bestscore = 200000
k = 5

scores = [1,10,100,1000]

data = ["","","BDDD","","BCBC","","DBAA","","AACC","",""]
objective = ["","","AAAA","","BBBB","","CCCC","","DDDD","",""]

#data = ["","","BD","","BC","","DA","","AC","",""]
#objective = ["","","AA","","BB","","CC","","DD","",""]

rooms = [2,4,6,8]
h = [0,1,3,5,7,9,10]


def containsOnly(s,c):
    for e in s:
        if e != c:
            return False
    return True
    
def possibleRoomToH(data,i,j):
    global rooms,h
    if data[i] == "" or containsOnly(data[i],chr(64+i//2)):
        return False
    possible = True
    for x in h:
        if ((x>i and x <= j) or (x < i and x >= j)) and data[x] != "":
            return False
    return True
    

def possibleHToRoom(data,i,j):
    global rooms,h
    c = data[i]
    s = data[j]
    if c == "" or len(s)==4 or c != chr(64+j//2) or not (containsOnly(s,c)):
        return False
    possible = True
    for x in h:
        if ((x>i and x <= j) or (x < i and x >= j)) and data[x] != "":
            return False
    return True

def computePossible(data):
    l = []
    global rooms,h
    for r in rooms:
        for e in h:
            if possibleRoomToH(data,r,e):
                l.append((r,e))
    for e in h:
        for r in rooms:
            if possibleHToRoom(data,e,r):
                l.append((e,r))
    return l
    
dico = {}

def lToH(l):
    s = ""
    for e in l:
        s += e + " "
    return s

def computeScore(data,m):
    global rooms,h
    global k
    i = m[0]
    j = m[1]
    c = data[i][0]
    factor = scores[ord(c)-ord('A')]
    if i in rooms:
        return factor*(abs(j-i)+k-len(data[i]))
    return factor*(abs(j-i) + k-1-len(data[j]))
   

    
def explore(data,current,d):
    global dico
    hashe = lToH(data)
    if hashe in dico:
        return dico[hashe]
    global objective,rooms,h,bestscore
    if data == objective:
        bestscore = min(bestscore,current)
        print(bestscore)
        return 0
    elif current < bestscore:
        moves = computePossible(data)
        mini = 100000000000
        for m in moves:
            #print(m)
            i,j=m
            s = computeScore(data,m)
            tmpi = data[i]
            tmpj = data[j]
            data[i] = data[i][1:]
            data[j] = tmpi[0] + tmpj
            mini = min(mini,s+explore(data,current+s,d+1))
            data[i] = tmpi
            data[j] = tmpj
        dico[hashe] = mini
        return mini
    else:
        return 1000000000
explore(data,0,0)
