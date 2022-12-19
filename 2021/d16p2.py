import re

l = []
file1 = open('data/exo31', 'r')
lines = file1.readlines()

def hexatobin(c):
    if c == "0":
            return "0000"
    elif c == "1":
            return "0001"
    elif c ==  "2":
            return "0010"
    elif c ==  "3":
            return "0011"
    elif c ==  "4":
            return "0100"
    elif c == "5":
            return "0101"
    elif c == "6":
            return "0110"
    elif c == "7":
            return "0111"
    elif c == "8":
            return "1000"
    elif c == "9":
            return "1001"
    elif c == "A":
            return "1010"
    elif c == "B":
            return "1011"
    elif c == "C":
            return "1100"
    elif c == "D":
            return "1101"
    elif c == "E":
            return "1110"
    elif c == "F":
            return "1111"

def binToInt(s):
    r = 0
    i = 0
    while i < len(s):
        r = 2*r + int(s[i])
        i += 1
    return r

data = ""
line = lines[0]
#line = "9C0141080250320F1802104A08\n"
i = len(line)-2
while i >= 0:
    data = hexatobin(line[i]) + data
    i-=1

sumversions = 0

def sum(l):
    r = 0
    for e in l:
        r += e
    return r

def product(l):
    r = 1
    for e in l:
        r *= e
    return r

def minimum(l):
    r = l[0]
    for e in l:
        r = min(r,e)
    return r

def maximum(l):
    r = l[0]
    for e in l:
        r = max(r,e)
    return r

def gt(l):
    return l[0] > l[1]

def lt(l):
    return l[1] > l[0]

def eq(l):
    return l[0] == l[1]

def decodeliteral(s,i):
    """
    retourne le premier indice après la fin du littéral
    """
    st = i
    r = 0
    while s[i] != "0":
        r = 16 * r + binToInt(s[i+1:i+5])
        i += 5
    r = 16 * r + binToInt(s[i+1:i+5])
    i = i+5
    return r,i


def decodeoperator(s,i,nbbits,nbsubpackets):
    start = i
    global sumversions
    l = []
    while i-start<nbbits-3 and nbsubpackets > 0:
        v = binToInt(s[i:i+3])
        sumversions += v
        i += 3
        typeid = binToInt(s[i:i+3])
        i += 3
        if typeid == 4:
            litt,i = decodeliteral(s,i)
            l.append(litt)
        else:
            if i >= len(s):
                return l
            b = s[i]
            i += 1
            if b == "0":
                bits = binToInt(s[i:i+15])
                i += 15
                listresults,i = decodeoperator(s,i,bits,float('inf'))
            else:
                subpackets = binToInt(s[i:i+11])
                i += 11
                listresults,i = decodeoperator(s,i,float('inf'),subpackets)
            if typeid == 0:
                l.append(sum(listresults))
            elif typeid == 1:
                l.append(product(listresults))
            elif typeid == 2:
                l.append(minimum(listresults))
            elif typeid == 3:
                l.append(maximum(listresults))
            elif typeid == 5:
                l.append(gt(listresults))
            elif typeid == 6:
                l.append(lt(listresults))
            elif typeid == 7:
                l.append(eq(listresults))
        nbsubpackets -= 1
    return l,i
           

def decode(s):
    return(decodeoperator(s,0,len(s),float('inf')))

decode(data)
print(sumversions)
