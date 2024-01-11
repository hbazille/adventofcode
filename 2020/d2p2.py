def is_ok(s, c, inf, sup):
    t_inf = inf < len(s) and s[inf] == c
    t_sup = sup < len(s) and s[sup] == c
    return abs(t_inf - t_sup)
    
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
        r += is_ok(s, c, inf-1, sup-1)
    print(r)
