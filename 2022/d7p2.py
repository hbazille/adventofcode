file1 = open('data/exo13', 'r')
lines = file1.readlines()


class Tree:
    def __init__(self, kind, name = "", weight = None):
        self.kind = kind
        self.name = name
        self.weight = weight
        self.children = []

filesystem = Tree("dir")

def print_tree(T, indent):
    print(indent, T.kind, T.name, T.weight)
    for e in T.children:
        print_tree(e, indent + "  ")
        
        
def make_tree(l, i, T):
    while i < len(l) - 1:
        line = lines[i].split()
        if line[0] == "$":
            if line [1] == "cd" and line[2] == "..":
                return i+1
            elif line[1] == "cd":
                j = 0
                while j < len(T.children) and T.children[j].name != line[2]:
                    j += 1
                if j < len(T.children):
                    i = make_tree(l, i+1, T.children[j])
            else:
                i += 1
                line = lines[i].split()
                while len(line) > 0 and line[0] != "$":
                    if line[0] == "dir":
                        T.children.append(Tree("dir", line[1]))
                    else:
                        T.children.append(Tree("file", line[1], int(line[0])))
                    i += 1
                    line = lines[i].split()
    return i           

    
def set_weight(T):
    if T.kind == "file":
        return T.weight
    else:
        w = 0
        for e in T.children:
            w += set_weight(e)
        T.weight = w
        return w

target = 30000000
best = 1000000000
def get_w(T, free, target):
    global best
    if T.kind == "file":
        return 0
    else:
        for e in T.children:
            get_w(e, free, target)
        if free + T.weight >= target and T.weight < best:
            best = T.weight
                        
make_tree(lines, 1, filesystem)
set_weight(filesystem)
free = 70000000 - filesystem.weight
get_w(filesystem, free, target)
print(best)
