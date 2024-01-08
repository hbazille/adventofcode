
def parseline(s, d):
    key = s[0:3]
    d["L"][key] = s[7:10]
    d["R"][key] = s[12:15]

def howmany(seq, start, end, d):
    c, i, n = 0, 0, len(seq) - 1
    while start != end:
        start = d[seq[i]][start]
        c += 1
        i = (i + 1) % n
    return c

if __name__ == "__main__":
    t = open('data/day8', 'r').readlines()
    d = {"L" : {}, "R" : {}}
    for line in t[2:]:
        parseline(line, d)
    print(howmany(t[0], "AAA", "ZZZ", d))
