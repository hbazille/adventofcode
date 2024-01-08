import re

def treat(line):
    i = 0
    j = len(line) - 1
    while line[i] not in "0123456789":
        i += 1
    while line[j] not in "0123456789":
        j -= 1
    return 10*int(line[i]) + int(line[j]) 

if __name__ == "__main__":
    file1 = open('data/day1', 'r')
    print(sum(treat(line) for line in file1))
        
