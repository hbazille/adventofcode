import re

l = []
file1 = open('data/exo27', 'r')
lines = file1.readlines()

dico = {}
rules = {}

def addDico(d,k,v):
    if k not in d:
        d[k] = v
    else:
        d[k] += v

i = 0
firstline = lines[0][:-1]
for i in range(len(firstline)-1):
    addDico(dico,firstline[i:i+2],1)
lastletter = firstline[-1]


for rule in lines[2:-1]:
    debut = rule[0:2]
    fin = rule[6]
    rules[debut] = fin

def transform(dico, rules):
    res = {}
    for (k,v) in dico.items():
        letter = rules[k]
        addDico(res,k[0]+letter,v)
        addDico(res,letter+k[1],v)
    return res

def mostleastcommon(histo):
    most = 0
    least = 100000000000000000000000
    for e in histo:
        if e != 0:
            most = max(e,most)
            least = min(e,least)
    return most-least

def histo(dico,lastletter):
    h = [0]*26
    for (k,v) in dico.items():
        h[ord(k[0])-ord('A')] += v
    h[ord(lastletter)-ord('A')] += 1
    return h

for i in range(40):
    dico = transform(dico,rules) 

print(mostleastcommon(histo(dico,lastletter)))
