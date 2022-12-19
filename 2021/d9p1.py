import re

l = []
file1 = open('data/day9', 'r')
lines = file1.readlines()

r = 0
data = []
inputs = []
outputs = []

for line in lines:
    l = line.split()
    data.append(l[0])

#data = ["2199943210","3987894921","9856789892","8767896789","9899965678"]


res = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        v = int(data[i][j])
        if (i==0 or v < int(data[i-1][j])) and (j==0 or v < int(data[i][j-1])) and ((i==len(data)-1) or v < int(data[i+1][j])) and ((j==len(data[0])-1) or v < int(data[i][j+1])):
            #print(i,j,v)
            res += v+1 
print(res)
