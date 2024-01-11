file1 = open('data/day11', 'r')
lines = file1.readlines()

class Monkey:
    def __init__(self, suc1, suc2, op, div, l = None):
        if l== None:
            self.l = []
        else:
            self.l = l
        self.suc1 = suc1
        self.suc2 = suc2
        self.div = div
        self.op = eval("lambda old : (" + op + ")//3")
        self.count = 0
            
def parse_items(l):
    r = []
    for i in l[2:-1]:
        r.append(int(i[:-1]))
    if len(l) >= 2:
        r.append(int(l[-1]))
    return r
        

def update(monkeys):
    for m in monkeys:
        m.count += len(m.l)
        for o in m.l:
            newo = m.op(o)
            if newo % m.div == 0:
                monkeys[m.suc1].l.append(newo)
            else:
                monkeys[m.suc2].l.append(newo)
        m.l = []


monkeys = []        
        
for i in range(8):
    items = parse_items(lines[7*i+1].split())
    div = int(lines[7*i+3].split()[-1])
    suc1 = int(lines[7*i+4].split()[-1])
    suc2 = int(lines[7*i+5].split()[-1])
    op = "".join(lines[7*i+2].split()[3:])
    monkeys.append(Monkey(suc1, suc2, op, div, items))
            
for i in range(20):
    update(monkeys)
t = [m.count for m in monkeys]
t.sort()
print(t[-1] * t[-2])
