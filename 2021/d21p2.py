import re

l = []
#file1 = open('data/exo39', 'r')
#lines = file1.readlines()
nb = [0,0,0,0,0,0,0,0,0,0]

for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            nb[i+j+k] += 1


# position1,position2,nbpoints1, nbpoints2, à qui le tour


p1 = 4
p2 = 10

def buildtab():
    scwp1 = []
    for i in range(11):
        pos1 = []
        for j in range(11):
            pos2 = []
            for k in range(21):
                s1 = []
                for l in range(21):
                    s1.append(0)
                pos2.append(s1)
            pos1.append(pos2)
        scwp1.append(pos1)
    return scwp1


scwp = buildtab()

scwp[4][10][0][0] = 1

win1 = 0
win2 = 0

def iterative(scwpt,t):
    global nb, win1, win2
    scwpr = buildtab()
    for pos1 in range(11):
        for pos2 in range(11):
            for score1 in range(21):
                for score2 in range(21):
                    nbcurrentuniv = scwp[pos1][pos2][score1][score2]
                    if nbcurrentuniv != 0:
                        for m in range(3,10):
                            if t == 0:
                                newpos = pos1 + m
                                if newpos > 10:
                                    newpos -= 10
                                newscore = score1 + newpos
                                nbuniv = nb[m] * nbcurrentuniv
                                if newscore >= 21:
                                    win1 += nbuniv
                                else:
                                    scwpr[newpos][pos2][newscore][score2] += nbuniv
                            else:
                                newpos = pos2 + m
                                if newpos > 10:
                                    newpos -= 10
                                newscore = score2 + newpos
                                nbuniv = nb[m] * nbcurrentuniv
                                if newscore >= 21:
                                    win2 += nbuniv
                                else:
                                    scwpr[pos1][newpos][score1][newscore] += nbuniv
    return scwpr


for i in range(19):
    scwp = iterative(scwp,i%2)
print(win1)

