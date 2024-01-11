file1 = open('data/exo1', 'r')
lines = file1.readlines()

maxi = [0, 0, 0]
k = 0
for line in lines:
    if len(line) > 1:
        k += int(line[:-1])
    else:
        if k > maxi[0]:
            maxi = [k, maxi[0], maxi[1]]
        elif k > maxi[1]:
            maxi = [maxi[0], k, maxi[1]]
        elif k > maxi[2]:
            maxi = [maxi[0], maxi[1], k]
        k = 0
print(maxi[0] + maxi[1] + maxi[2])
