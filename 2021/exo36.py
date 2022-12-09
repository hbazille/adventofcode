import re

l = []
file1 = open('data/exo35', 'r')
lines = file1.readlines()

class BinTree:

    def __init__(self, key, left=None, right=None):
        """
        Init Tree
        """
        self.key = key
        self.left = left
        self.right = right

def pp(T,indent):
    if T == None:
        pass
    else:
        print(indent,T.key)
        pp(T.left,indent+"  ")
        pp(T.right,indent+"  ")

def __parse(s,i):
    t = BinTree(None,None,None)
    if s[i] == "[":
        i,tleft = __parse(s,i+1)
        t.left = tleft
    else:
        t.left = BinTree(int(s[i]),None,None)
        i += 1
    i += 1
    if s[i] == "[":
        i,tright = __parse(s,i+1)
        t.right = tright
    else:
        t.right = BinTree(int(s[i]),None,None)
        i += 1
    return i+1,t

def parse(s):
    return __parse(s,1)[1]

def changeFirstLeft(T,x):
    while T.key == None:
        T = T.left
    T.key += x

def changeFirstRight(T,x):
    while T.key == None:
        T = T.right
    T.key += x

def __checkAndExplode(T,depth):
    found = False
    if T.key != None:
        return False, None, None
    if depth == 4:
        if T.key == None:
            kl,kr = T.left.key, T.right.key
            T.key = 0
            T.left = None
            T.right = None
            return True, kl, kr
        else:
            return False, None, None
    else:
        hasExploded, kl, kr = __checkAndExplode(T.left,depth+1)
        if hasExploded:
            if kr != None:
                changeFirstLeft(T.right,kr)
            return True, kl, None
        hasExploded, kl, kr = __checkAndExplode(T.right,depth+1)
        if hasExploded:
            if kl != None:
                changeFirstRight(T.left,kl)
            return True, None, kr
        return False, None, None
        
def checkAndExplode(T):
    a,b,c = __checkAndExplode(T,0)
    return a

def split(T):
    if T.key != None:
        if T.key >= 10:
            kl = T.key//2
            kr = (T.key+1)//2
            T.key = None
            T.left = BinTree(kl)
            T.right = BinTree(kr)
            return True
        return False
    if split(T.left):
        return True
    if split(T.right):
        return True
    return False

def reduce(T):
    while checkAndExplode(T) or split(T):
        pass

def add(T1,T2):
    return BinTree(None,T1,T2)
    
def magnitude(T):
    if T.key != None:
        return T.key
    return 3*magnitude(T.left) + 2*magnitude(T.right)

def copy(T):
    if T == None:
        return None
    return BinTree(T.key,copy(T.left),copy(T.right))

listentries = []
for l in lines[:-1]:
    listentries.append(parse(l[:-1]))

bestmagnitude = 0
i = 0
while i < 100:
    j = 0
    while j < 100:
        if j != i:
            Ti = copy(listentries[i])
            Tj = copy(listentries[j])
            T = add(Ti,Tj)
            reduce(T)
            m = magnitude(T)
            bestmagnitude = max(m,bestmagnitude)
        j += 1
    i += 1
print(bestmagnitude)
