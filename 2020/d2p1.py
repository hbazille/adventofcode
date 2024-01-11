def nb_occ(s, c):
    return sum(c == s[i] for i in range(len(s)))

def parse(line):
    t = line.split()
    d = t[0].split("-")
    return int(d[0]), int(d[1]), t[1][0], t[2]
    
if __name__ == "__main__":
    file = open('data/day2', 'r')
    lines = file.readlines()
    r = 0
    for line in lines[:-1]:
        inf, sup, c, s = parse(line)
        r += inf <= nb_occ(s, c) <= sup
    print(r)
