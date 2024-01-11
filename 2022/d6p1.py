file1 = open('data/day6', 'r')
lines = file1.readlines()

st = []

line = lines[0]

def double(l):
    l2 = []
    for e in l:
        l2.append(e)
    l2.sort()
    i = 0
    while i < len(l) - 1 and l2[i] != l2[i+1]:
        i += 1
    return i >= len(l) - 1

chars = []

i = 0
while i < len(line) - 3:
    c = line[i]
    chars.append(c)
    if len(chars) == 4:
        if double(chars):
            print(i+1)
            break
        chars.pop(0)
    i += 1
