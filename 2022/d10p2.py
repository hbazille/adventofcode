file1 = open('data/exo19', 'r')
lines = file1.readlines()

cycle = 0
x = 1

l = [" "]*240

def pp240(l):
    for i in range(6):
        for j in range(40):
            print(l[40*i+j], end="")
        print()

for line in lines[:-1]:
    s = line.split()
    if s[0] == "noop":
        if x-1 <= cycle%40 <= x+1:
            l[cycle] = "#"
        else:
            l[cycle] = "."
        cycle += 1
    else:
        if x-1 <= cycle%40 <= x+1:
            l[cycle] = "#"
        else:
            l[cycle] = "."
        cycle += 1
        if  x-1 <= cycle%40 <= x+1:
            l[cycle] = "#"
        else:
            l[cycle] = "."
        cycle += 1
        x += int(s[1])
#    print(x, cycle)
  
pp240(l)
        
