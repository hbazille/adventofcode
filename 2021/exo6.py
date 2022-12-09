
l = []
file1 = open('data/exo5', 'r')
lines = file1.readlines()


l0 = []
l1 = []
for line in lines:
    li = line.split()
    if li != []:
        l0.append(li[0])
        l1.append(li[0])

m = len(l0[0])
i = 0


def copy(l,c,i):
    lres = []
    for e in  l:
        if e[i] == c:
            lres.append(e)
    return lres


def filter(l):
    global m
    for j in range(m):
        i = 0
        uns = 0
        zeros = 0
        while(i<len(l)):
            if l[i][j] == "1":
                uns += 1
            else:
                zeros += 1
            i += 1
        if uns>=zeros:
            l = copy(l,"1",j)
        else:
            l = copy(l,"0",j)
    return l[0]

def filterleast(l):
    global m
    j = 0
    while j <m and len(l)>1:
        i = 0
        uns = 0
        zeros = 0
        while(i<len(l)):
            if l[i][j] == "1":
                uns += 1
            else:
                zeros += 1
            i += 1
        if uns<zeros:
            l = copy(l,"1",j)
        else:
            l = copy(l,"0",j)
        j += 1
    return l[0]

def tobin(s):
    r = 0
    i = 0
    while i < len(s):
        r *= 2
        if s[i] == "1":
            r += 1
        i += 1
    return r

print(tobin(filter(l0))*tobin(filterleast(l1)))
