
l = []
file1 = open('data/exo5', 'r')
lines = file1.readlines()


for line in lines:
    li = line.split()
    if li != []:
        l.append(li[0])

m = len(l[0])
zeros=[0]*len(l[0])
uns=[0]*len(l[0])
i = 0
n = len(l)
m = len(l[0])

while(i<n):
    for j in range(m):
        if l[i][j] == "1":
            uns[j] += 1
        else:
            zeros[j] += 1
    i += 1

r = 0
j = 0
e = 0
while j < m:
    r *= 2
    e *= 2
    if uns[j] > zeros[j]:
        r += 1
    else:
        e += 1
    j+=1
print(r*e)
