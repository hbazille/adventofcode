file1 = open('data/day2', 'r')
lines = file1.readlines()

score = {'X' : 1, 'Y' : 2, 'Z' : 3}

def compare(u, v):
    i = ord(u) - ord('A')
    j = ord(v) - ord('X')
    if i == j:
        return 3
    elif (j-i)%3 == 1:
        return 6
    else:
        return 0

sc = 0 
for line in lines[:-1]:
    u = line[0]
    v = line[2]
    sc += score[v] + compare(u, v)
print(sc)   
