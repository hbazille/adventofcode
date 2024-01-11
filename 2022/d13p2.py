from functools import cmp_to_key
file1 = open('data/exo25', 'r')
lines = file1.readlines()

class Tree:
    def __init__(self, key, children = None):
        self.key = key
        if children == None:
            self.children = []
        else:
            self.children = children


def parse(line, i, T):
    while i < len(line):
        if line[i] == "[":
            Tson = Tree("list")
            i = parse(line, i + 1, Tson)
            T.children.append(Tson)
        elif line[i] == "]":
            return i + 1
        elif line[i] == ",":
            i += 1
        else:
            while line[i] not in ",]":
                n = 0
                while "0" <= line[i] <= "9":
                    n = 10*n + int(line[i])
                    i += 1 
            T.children.append(Tree(n))
    


def pp(T, indent):
    if T == None:
        return
    print(indent, T.key)
    for c in T.children:
        pp(c, indent + "  ")
    
    
def compare(Tl, Tr):
    if Tl.key == "list" and Tr.key == "list":
        i = 0
        while i < len(Tl.children) and i < len(Tr.children):
            k = compare(Tl.children[i], Tr.children[i])
            if k != 0:
                return k
            i += 1
        if i == len(Tl.children):
            if i == len(Tr.children):
                return 0
            return 1
        return -1
    if Tl.key == "list":
        if Tl.children == []:
            return 1
        Trbis = Tree("list", [Tr])
        return compare(Tl, Trbis)
    if Tr.key == "list":
        if Tr.children == []:
            return -1
        Tlbis = Tree("list", [Tl])
        return compare(Tlbis, Tr)
    if Tl.key == Tr.key:
        return 0
    if Tl.key < Tr.key:
        return 1
    return -1

i = 0
liste = []
while i < len(lines) - 1:
    l = lines[i][:-1]
    Tl = Tree("list")
    parse(l, 1, Tl)
    r = lines[i+1][:-1]
    Tr = Tree("list")
    parse(r, 1, Tr)
    liste += [Tl, Tr]
    i += 3

T2 = Tree("list")
parse("[[2]]", 1, T2)
T6 = Tree("list")
parse("[[6]]", 1, T6)
liste += [T2, T6]

def insertsort(l, c):
    i = 1
    while i < len(l):
        j = i
        while j > 0 and c(l[j], l[j-1]) == 1:
            l[j], l[j-1] = l[j-1], l[j]
            j -= 1
        i += 1

insertsort(liste, compare)

i2, i6 = 0, 0
for i in range(len(liste)):
    if liste[i] == T2:
        i2 = i + 1
    elif liste[i] == T6:
        i6 = i + 1
print(i2*i6)
