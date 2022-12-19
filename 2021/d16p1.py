import re

l = []
file1 = open('data/day16', 'r')
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
#line = "A0016C880162017C3686B18A3D4780\n"
i = len(line)-2
while i >= 0:
    data = hexatobin(line[i]) + data
    i-=1

sumversions = 0

def decodeliteral(s,i):
    """
    retourne le premier indice après la fin du littéral
    """
    st = i
    while s[i] != "0":
        i += 5
    i = i+5
    #while (i-st)%4 != 0:
    #    i += 1
    return i

def decodeoperatorpackets(s,i,nbsubpackets):
    global sumversions
    v = binToInt(s[i:i+3])
    sumversions += v
    i += 3
    typeid = binToInt(s[i:i+3])
    i += 3
    if typeid == 4:
        i = decodeliteral(s,i)


def decodeoperator(s,i,nbbits,nbsubpackets):
    start = i
    global sumversions
    while i-start<nbbits-3 and nbsubpackets > 0:
        v = binToInt(s[i:i+3])
        sumversions += v
        i += 3
        typeid = binToInt(s[i:i+3])
        i += 3
        if typeid == 4:
            i = decodeliteral(s,i)
        else:
            b = s[i]
            i += 1
            if b == "0":
                bits = binToInt(s[i:i+15])
                i += 15
                i = decodeoperator(s,i,bits,float('inf'))
            else:
                subpackets = binToInt(s[i:i+11])
                i += 11
                i = decodeoperator(s,i,float('inf'),subpackets)
        nbsubpackets -= 1
    return i
           

def decode(s):
    decodeoperator(s,0,len(s),float('inf'))

decode(data)
print(sumversions)
