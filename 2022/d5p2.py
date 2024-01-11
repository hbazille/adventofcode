file1 = open('data/exo9', 'r')
lines = file1.readlines()

st = []

def ps(s):
    for stack in s:
        for e in stack:
            print(e, end ="")
        print()

l = len(lines[0])
for _ in range(l//4):
    st.append([])

i = 0
while lines[i][1] != "1":
    line = lines[i]
    for j in range(9):
        box = line[4*j+1]
        if box != " ":
            st[j].append(box)
    i += 1
for i in range(9):
    st[i].reverse()
    
i += 2
while i < len(lines) - 1:
    line = lines[i].split()
    nb = int(line[1])
    a = int(line[3])-1
    b = int(line[5])-1
    for j in range(nb):
        la = len(st[a])
        st[b].append(st[a][la-nb+j])
    for j in range(nb):
        st[a].pop()
    i += 1
ps(st)
