from math import sqrt, ceil, floor

def parseline(s):
    return int("".join(w for w in s.strip().split()[1:]))  
                

def roots(t, d):
    delta = sqrt(t*t - 4*d)
    return floor((t + delta)/2) - ceil((t - delta)/2) + 1 
   

if __name__ == "__main__":
    file1 = open('data/day6', 'r')
    lines = file1.readlines()
    print(roots(parseline(lines[0]), parseline(lines[1])))
