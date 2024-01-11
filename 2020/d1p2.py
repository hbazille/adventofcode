
if __name__ == "__main__":
    file = open('data/day1', 'r')
    lines = file.readlines()
    l = []
    for line in lines[:-1]:
        l.append(int(line[:-1]))
    l.sort()
    i, found = 0, False
    while i < len(l) and not found:
        j = i + 1 
        while j < len(l) and not found:
            k = j + 1
            while l[i] + l[j] + l[k] < 2020:
                k += 1
            if k < len(l) and l[i] + l[j] + l[k] == 2020:
                print(l[i] * l[j] * l[k])
                found = True
            j += 1
        i += 1 
