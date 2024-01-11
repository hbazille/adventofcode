l = []
file1 = open('data/day1', 'r')
lines = file1.readlines()

maxi = 0
k = 0
for line in lines:
    if len(line) > 1:
        k += int(line[:-1])
    else:
        maxi = max(k,maxi)
        k = 0
print(maxi)
