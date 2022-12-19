import re

l = []
file1 = open('data/exo15', 'r')
lines = file1.readlines()

r = 0

bias = ord('a')
inputs = []
outputs = []

for line in lines:
    l = line.split("|")
    inputs.append(l[0].split())
    outputs.append(l[1].split())


#inputs = [["acedgfb", "cdfbe", "gcdfa", "fbcad", "dab", "cefabd", "cdfgeb", "eafb", "cagedb", "ab"]]
#outputs = [["cdfeb", "fcadb", "cdfeb", "cdbaf"]]

def count(l,a):
    r = 0
    for e in l:
        for c in e:
            r += c == a
    return r

def chiffre(word, dico):
    if len(word) == 2:
        return 1
    elif len(word) == 3:
        return 7
    elif len(word) == 7:
        return 8
    elif len(word) == 4:
        return 4
    elif len(word) == 5: # 2 : 35   3 :38   5 :32
        c = 0   
        for e in word:
            c += dico[e]
        if c == 37:
            return 5
        elif c == 39:
            return 3
        else:
            return 2
    else: # 0 : 41    6 : 41    9 : 44
        c = 0   
        for e in word:
            c += dico[e]
        if c == 45:
            return 9
        elif c== 42:
            return 0
        else:
            return 6
        

def treatline(inp, out):
    dico = {}
    for e in "abcdefg":
        dico[e] = count(inp,e)
    #print(dico)
    r = 0
    for c in out:
        r = r*10+chiffre(c,dico)
    return r

i = 0
res = 0
while i < len(inputs):
    res += treatline(inputs[i],outputs[i])
    i += 1
print(res)

"""
top : 8
top left : 6
top right : 8
mid : 7
bottom left : 4
bottom right : 9
bottom : 7)
"""
