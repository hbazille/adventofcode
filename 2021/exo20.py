import re

l = []
file1 = open('data/exo19', 'r')
lines = file1.readlines()

r = 0
data = []
inputs = []
outputs = []

for line in lines:
    l = line.split()
    data.append(l[0])

#data = ["[({(<(())[]>[[{[]{<()<>>","[(()[<>])]({[<{<<[]>>(","(((({<>}<{<{<>}{[]{[]{}","{<[[]]>}<{[{[{[]{()[[[]","<{([{{}}[<[[[<>{}]]]>[]]"]
points = {}
points[")"] = 1
points["]"] = 2
points["}"] = 3
points[">"] = 4
other = {}
other["("] = ")"
other["["] = "]"
other["{"] = "}"
other["<"] = ">"


def parseold(s,i):
    if i >= len(s):
        return True, 0, i
    c = s[i]
    i += 1
    if i >= len(s):
        return True, 0, i
    cnext = s[i]
    while cnext not in ")>}]":
        noerror, point, i = parseold(s,i)
        if not noerror:
            return False, point, i 
        if i >= len(s):
            return True, 0, i
        cnext = s[i]
    if other[c] != cnext:
        return False, points[cnext], i
    else:
        return True, 0, i+1
    

def parse(s,i):
    if i >= len(s):
        return True, 0, i
    c = s[i]
    i += 1
    if i >= len(s):
        return False, points[other[c]], i
    cnext = s[i]
    while cnext not in ")>}]":
        noerror, point, i = parse(s,i)
        #print(noerror,point,i)
        if not noerror:
            return False, point*5 + points[other[c]], i 
        if i >= len(s):
            return False, points[other[c]], i
        cnext = s[i]
    if other[c] != cnext:
        return True, 0, i+1
    else:
        return True, 0, i+1
    
    
l = []
for e in data:
    if parseold(e,0)[1]==0:
        i = 0
        p = 0
        while i < len(e):
            b,p,i = parse(e,i)
        l.append(p)
l.sort()
print(l[len(l)//2])
