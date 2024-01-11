
if __name__ == "__main__":
    file = open('data/day1', 'r')
    lines = file.readlines()
    l = []
    for line in lines[:-1]:
        l.append(int(line[:-1]))
    l.sort()
    i, found = 0, False
    while i < len(l) and not found:
        j = i+1 
        while j < len(l) and l[i] + l[j] < 2020:
            j += 1
        if j < len(l) and l[i] + l[j] == 2020:
            print(l[i] * l[j])
            found = True
        i += 1 
