
def ok_unit(t, cols):
    return cols[t[1]] >= int(t[0])    

def ok_round(s, cols):
    return all(ok_unit(w.split(), cols) for w in s.split(","))

def ok_game(s, cols):
    return all(ok_round(w.strip(), cols) for w in s[s.index(":") + 2 :].split(";"))
    
    
if __name__ == "__main__":
    file1 = open('data/day2', 'r')
    s = 0
    i = 1
    d = {"red": 12, "green": 13, "blue": 14}
    for line in file1:
        if ok_game(line, d):
            s += i
        i += 1
    print(s)
        
