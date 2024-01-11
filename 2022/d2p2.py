file1 = open('data/exo3', 'r')
lines = file1.readlines()

score = {'X' : 0, 'Y' : 3, 'Z' : 6}

def compare(u, v):
    if v == 'Z':
        x = 1
    elif v == 'Y':
        x = 0
    else:
        x = -1
    i = ord(u) + x
    if i == ord('C') or i < ord('A'):
        return 3
    elif i == ord('B'):
        return 2
    else: 
        return 1
    

#lines = ["A Y ", "B X ", "C Z", ""]
sc = 0 
for line in lines[:-1]:
    u = line[0]
    v = line[2]
    sc += score[v] + compare(u, v)
print(sc)   
