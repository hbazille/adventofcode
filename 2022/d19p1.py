import math

def parse(line):
    t = line.split()
    return int(t[6]), int(t[12]), int(t[18]), int(t[21]), int(t[-5]), int(t[-2]),


def _dynprog(blueprint, robots, reserves, time, biggest, d):
    if time < 0:
        return 0
    elif time == 0:
        return reserves[3]
    if (robots, reserves, time) in d:
        return d[(robots, reserves, time)]
    ro, rc, rob, rg = robots
    no, nc, nob, ng = reserves
    bo, bc, bob = biggest
    best = rg * time + ng
    if rob > 0:
        wait = max(0, -((no - blueprint[4]) // ro), -((nob - blueprint[5]) // rob))
        best = max(best, _dynprog(blueprint, (ro, rc, rob, rg + 1), (no - blueprint[4] + (wait + 1) * ro, nc + (wait + 1) * rc, nob +  + (wait + 1) * rob - blueprint[5], ng +  + (wait + 1) * rg), time -  + (wait + 1), biggest, d))
    if rob < bob and rc > 0:
        wait = max(0, -((no - blueprint[2]) // ro), -((nc - blueprint[3]) // rc))
        best = max(best, _dynprog(blueprint, (ro, rc, rob + 1, rg), (no - blueprint[2] + (wait + 1) * ro, nc - blueprint[3] + (wait + 1) * rc, nob + (wait + 1) * rob, ng + (wait + 1) * rg), time - (wait + 1), biggest, d))
    if ro < bo:
        wait = max(0, -((no - blueprint[0]) // ro))
        best = max(best, _dynprog(blueprint, (ro + 1, rc, rob, rg), (no - blueprint[0] + (wait + 1) * ro, nc + (wait + 1) * rc, nob + (wait + 1) * rob, ng + (wait + 1) * rg), time - (wait +1), biggest, d))
    if rc < bc:
        wait = max(0, -((no - blueprint[1]) // ro))
        best = max(best, _dynprog(blueprint, (ro, rc + 1, rob, rg), (no - blueprint[1] + (wait + 1) * ro, nc + (wait + 1) * rc, nob + (wait + 1) * rob, ng + (wait + 1) * rg), time - (wait +1), biggest, d))
    d[(robots, reserves, time)] = best
    return best
    
    
def dynprog(blueprint, time):
    d = {}
    robots = (1, 0, 0, 0)
    reserves = (0, 0, 0, 0)
    bo = max(blueprint[0], blueprint[1], blueprint[2], blueprint[4])
    bc = blueprint[3]
    bob = blueprint[5]
    return _dynprog(blueprint, robots, reserves, time, (bo, bc, bob), d)


if __name__ == '__main__':
    file1 = open('data/day19', 'r')
    lines = file1.readlines()
    idb = 0
    sum_prod = 0
    for line in lines[:-1]:
        n = dynprog(parse(line[:-1]), 24)
        idb += 1
        sum_prod += n * idb
    print(sum_prod)
