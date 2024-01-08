from math import sqrt, floor, ceil
from functools import reduce
import operator

def parseline(s):
    return list(map(lambda x : int(x), s.strip().split()[1:]))
    
def roots(t, d):
    delta = sqrt(t*t - 4*d)
    return floor((t + delta)/2) - ceil((t - delta)/2) + 1 

if __name__ == "__main__":
    file1 = open('data/day6', 'r')
    lines = file1.readlines()
    print(reduce(operator.mul, [roots(t, d) for (t, d) in zip(parseline(lines[0]), parseline(lines[1]))]))
    
