
l = []
file1 = open('data/exo3', 'r')
lines = file1.readlines()


for line in lines:
    li = line.split()
    li[1] = int(li[1])
    l.append(li)

i = 0
n = len(l)
h = 0
d = 0

while(i<n):
    way = l[i][0]
    x = l[i][1]
    if way == "forward":
        h += x
    elif way == "up":
        d -= x
    else:
        d += x
    i += 1
print(h*d)
