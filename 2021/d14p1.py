import re

l = []
file1 = open('data/day14', 'r')
lines = file1.readlines()

chain = ""
rules = {}

for c in lines[0][:-1]:
    chain += c

for rule in lines[2:-1]:
    debut = rule[0:2]
    fin = rule[6]
    rules[debut] = fin

def transform(chain, rules):
    res = ""
    for i in range(len(chain)-1):
        res += chain[i] + rules[chain[i:i+2]]
    res += chain[-1]
    return res

def mostleastcommon(histo):
    most = 0
    least = 100000000000000000000000
    for e in histo:
        if e != 0:
            most = max(e,most)
            least = min(e,least)
    return most-least

def histo(s):
    h = [0]*26
    for c in s:
        h[ord(c)-ord('A')] += 1
    return h

for i in range(10):
    chain = transform(chain,rules) 

print(mostleastcommon(histo(chain)))
