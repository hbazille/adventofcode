

def from_unit(s, cols):
    r, g, b = cols
    t = s.split()
    if t[1] == "red":
        return max(int(t[0]), r), g, b
    if t[1] == "green":
        return r, max(int(t[0]), g), b
    return r, g, max(int(t[0]), b)
    

def from_round(s, cols):
    r, g, b = cols
    for w in s.split(","):
        r, g, b = from_unit(w, (r, g, b))
    return r, g, b

def from_game(s):
    r, g, b = 0, 0, 0
    for w in s[s.index(":") + 2:].split(";"):
        r, g, b = from_round(w.strip(), (r, g, b))
    return r * g * b
    
if __name__ == "__main__":
    file1 = open('data/day2', 'r')
    print(sum(from_game(line) for line in file1))
        
