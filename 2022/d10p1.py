file1 = open('data/day10', 'r')
lines = file1.readlines()

sum = 0
cycle = 0
x = 1
timers = [20, 60, 100, 140, 180, 220]

for line in lines[:-1]:
    s = line.split()
    if s[0] == "noop":
        cycle += 1
        if cycle in timers:
            sum += x * cycle
            #print(x, cycle)
    else:
        if cycle +1 in timers:
            sum += x * (cycle+1)
            #print(x, cycle+1)
        if  cycle+2 in timers:
            sum += x * (cycle + 2)
            #print(x, cycle + 2)
        x += int(s[1])
        cycle += 2
#    print(x, cycle)
  
print(sum)
        
