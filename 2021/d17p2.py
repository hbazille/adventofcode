import re

l = []
#file1 = open('data/exo33', 'r')
#lines = file1.readlines()

xmin = 236
xmax = 262

ymin = -78
ymax = -58

def tryshot(x,y,vx,vy):
    #print (x,y)    
    global xmin,xmax,ymin,ymax
    if y < ymin or x>xmax:
        return 0
    if x >= xmin and x <= xmax and y >= ymin and y<= ymax:
        return 1
    x += vx
    y += vy
    if vx > 0:
        vx -= 1
    vy -= 1
    return tryshot(x,y,vx,vy)

r = 0

for vx in range(22,263):
    for vy in range(-78,79):
        r += tryshot(0,0,vx,vy)

print(r)
