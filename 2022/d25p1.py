
def convert(s, d):
    r = 0
    for e in s:
        r = r * 5 + d[e]
    return r
    
def addone(v):
    match v:
        case "0": 
            return "1", 0
        case "1":
            return "2", 0
        case "2":
            return "1=", 0
        case "1=":
            return "1-", 0
        case "1-":
            return "0", 1
    
def add(l):
    r = 0
    s = ""
    i = 0
    while i < len(l):
        v = l[i]
        s += v[-1]
        if len(v) > 1:
            r = 1
            j = i + 1
            while j < len(l) and r:
                l[j], r = addone(l[j])
                j += 1
            if j == len(l) and r:
                l.append("1")
        i += 1
    return s[::-1]
    
def convertback(n, d):
    l = []
    while n > 0:
        l.append(d[n % 5])
        n = n // 5
    return add(l)
        
if __name__ == '__main__':
    file = open('data/day25', 'r')
    lines = file.readlines()
    d = {"0" : 0, "1" : 1, "2" : 2, "-" : -1, "=" : -2}
    d2 = ["0", "1", "2", "1=", "1-"]
    print(convertback(sum(convert(line[:-1], d) for line in lines[:-1]), d2))
        
