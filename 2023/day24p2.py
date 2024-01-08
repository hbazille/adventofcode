
import sympy



def solve(d):
    x, y, z = sympy.var('x'), sympy.var('y'), sympy.var('z')
    dx, dy, dz = sympy.var('dx'), sympy.var('dy'), sympy.var('dz')
    k1, k2, k3 = sympy.var('k1'), sympy.var('k2'), sympy.var('k3')
    p1, p2, p3 = d[0], d[2], d[3]
    equations = [sympy.Eq(x + k1*dx, p1[0] + p1[3]*k1), sympy.Eq(y + k1*dy, p1[1] + p1[4]*k1),\
                sympy.Eq(z + k1*dz, p1[2] + p1[5]*k1), sympy.Eq(x + k2*dx, p2[0] + p2[3]*k2), \
                sympy.Eq(y + k2*dy, p2[1] + p2[4]*k2), sympy.Eq(z + k2*dz, p2[2] + p2[5]*k2), \
                sympy.Eq(x + k3*dx, p3[0] + p3[3]*k3), sympy.Eq(y + k3*dy, p3[1] + p3[4]*k3), \
                sympy.Eq(z + k3*dz, p3[2] + p3[5]*k3)]
    d = sympy.solve(equations)[0]
    return sum(d[v] for v in (x, y, z))
    

def parseline(s):
    t = s.split("@")
    return tuple(list(map(lambda x : int(x.strip()), t[0].split(","))) + list(map(lambda x : int(x.strip()), t[1].split(",")))) 
                 
                 
if __name__ == "__main__":
    l = [parseline(s.strip()) for s in open('data/day24', 'r').readlines()]
    print(solve(l))
