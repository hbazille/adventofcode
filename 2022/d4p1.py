file1 = open('data/day4', 'r')
lines = file1.readlines()


sc = 0
i = 0
for line in lines[:-1]:
    s = line[:-1].split(",")
    r1 = s[0].split("-")
    r2 = s[1].split("-")
    a = int(r1[0])
    b = int(r1[1])
    c = int(r2[0])
    d = int(r2[1])
    sc += (a <= c and b >= d) or (a >= c and b <= d)
print(sc)   
