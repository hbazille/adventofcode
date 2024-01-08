
def hashia(s):
    r = 0
    for c in s:
        r = ((r + ord(c)) * 17) % 256
    return r    
    

if __name__ == "__main__":
    print(sum(hashia(s) for s in open('data/day15', 'r').readlines()[0].strip().split(",")))
    
