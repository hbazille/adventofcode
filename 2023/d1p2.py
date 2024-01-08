import re


def isvalidst(l, i):
    n = len(l)
    if l[i] in "123456789":
        return int(l[i])
    if i + 2 < n:
        if l[i:i+3] == "six":
            return 6
        if l[i:i+3] == "one":
            return 1
        if l[i:i+3] == "two":
            return 2
    if i + 3 < n:
        if l[i:i+4] == "four":
            return 4
        if l[i:i+4] == "five":
            return 5
        if l[i:i+4] == "nine":
            return 9
    if i + 4 < n:
        if l[i:i+5] == "eight":
            return 8
        if l[i:i+5] == "three":
            return 3
        if l[i:i+5] == "seven":
            return 7
    return None




def isvalidend(l, i):
    n = len(l)
    if l[i] in "123456789":
        return int(l[i])
    if i > 1:
        if l[i-2:i+1] == "six":
            return 6
        if l[i-2:i+1] == "one":
            return 1
        if l[i-2:i+1] == "two":
            return 2
    if i > 2:
        if l[i-3:i+1] == "four":
            return 4
        if l[i-3:i+1] == "five":
            return 5
        if l[i-3:i+1] == "nine":
            return 9
    if i > 3:
        if l[i-4:i+1] == "eight":
            return 8
        if l[i-4:i+1] == "three":
            return 3
        if l[i-4:i+1] == "seven":
            return 7
    return None



def treat(line):
    i = 0
    j = len(line) - 1
    si = None
    sj = None
    while i < len(line) and si == None:
        si = isvalidst(line, i)
        i += 1
    while j >= 0 and sj == None:
        sj = isvalidend(line, j)
        j -= 1
    return 10*si + sj 

if __name__ == "__main__":
    file1 = open('data/day1', 'r')
    print(sum(treat(line) for line in file1))
        
