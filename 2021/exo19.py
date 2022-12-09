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

#data = ["[({(<(())[]>[[{[]{<()<>>","[(()[<>])]({[<{<<[]>>(","{([(<{}[<>[]}>{[]{[(<()>","(((({<>}<{<{<>}{[]{[]{}","[[<[([]))<([[{}[[()]]]","[{[{({}]{}}([{[{{{}}([]","{<[[]]>}<{[{[{[]{()[[[]","[<(<(<(<{}))><([]([]()","<{([([[(<>()){}]>(<<{{","<{([{{}}[<[[[<>{}]]]>[]]"]
points = {}
points[")"] = 3
points["]"] = 57
points["}"] = 1197
points[">"] = 25137
other = {}
other["("] = ")"
other["["] = "]"
other["{"] = "}"
other["<"] = ">"

def parse(s,i):
    if i >= len(s):
        return True, 0, i
    c = s[i]
    i += 1
    if i >= len(s):
        return True, 0, i
    cnext = s[i]
    while cnext not in ")>}]":
        noerror, point, i = parse(s,i)
        if not noerror:
            return False, point, i 
        if i >= len(s):
            return True, 0, i
        cnext = s[i]
    if other[c] != cnext:
        return False, points[cnext], i
    else:
        return True, 0, i+1
    
    
r = 0
for e in data:
    r += parse(e,0)[1]
print(r)
