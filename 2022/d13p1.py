file1 = open('data/day13', 'r')
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
count = 0
while i < len(lines) - 1:
    l = lines[i][:-1]
    Tl = Tree("list")
    parse(l, 1, Tl)
    r = lines[i+1][:-1]
    Tr = Tree("list")
    parse(r, 1, Tr)
    if(compare(Tl, Tr))>0:
        count += i//3 + 1
        print("yay", i)
    else:
        print("nay", i)
    i += 3
print(count)

