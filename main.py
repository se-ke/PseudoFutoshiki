from pysat.solvers import Solver, MapleChrono
from pysat.formula import CNF
from pysat.pb import *
from pysat.formula import IDPool


# 1. Read file character
# 2. Determine pre-existing cell values and constraints
# 3. Given the pre-existing cell values and constraints, create CNF formula
# 4. Feed that CNF formula into SAT solver

def s(x, y, z):
    if z == "_":
        z = 0
    return (n * n) * x + n * y + int(z)


def read_file(file_name):
    with open(file_name, 'r') as f:
        fic = f.read().split('\n')
    return fic


def get_grid(f):
    global n

    def h(i, j):
        return (i // 2), (j // 2)

    v, c, n = [], [], (len(f) + 1) // 2

    for i in range(len(f)):
        ll = []
        if i % 2 == 0:
            for j in range(len(f[i])):
                if f[i][j] != ' ':
                    if f[i][j] == '<':
                        c.append([h(i, j + 1), h(i, j - 1)])
                    elif f[i][j] == '>':
                        c.append([h(i, j - 1), h(i, j + 1)])
                    else:
                        ll.append(f[i][j])
            v.append(ll)
        else:
            for j in range(len(f[i])):
                if f[i][j] == '^':
                    c.append([h(i + 1, j), h(i - 1, j)])
                if f[i][j] == 'v' or f[i][j] == 'V':
                    c.append([h(i - 1, j), h(i + 1, j)])
    return v, c


def get_clause(v, c):
    p = CNF()
    vpool = IDPool()
    for i in range(n):
        for j in range(n):
            if v[i][j] != "_":
                vpool.id('v{0}'.format(s(i, j, v[i][j])))
                p.extend(PBEnc.equals(lits=[s(i, j, v[i][j])], bound=1, vpool=vpool).clauses)
    # one value per square
    for x in range(n):
        for y in range(n):
            lits = []
            for z in range(1, n + 1):
                lits.append(s(x, y, z))
            p.extend(PBEnc.equals(lits=lits, bound=1, vpool=vpool).clauses)
    # one value per line
    for y in range(n):
        lits = []
        weights = []
        for z in range(1, n + 1):
            for x in range(n):
                lits.append(s(x, y, z)) # row 1, column 1 -> row 2 column 1 -> row 3 column 1 -> ... -> row n column 1
                weights.append(z)
                #lits2.append(s(y, x, z)) # row 1, column 1 -> row 1 column 2 -> row 1 column 3 -> ... -> row 1 column n
        p.extend(PBEnc.equals(lits=lits, weights=weights, bound=int((n * (n + 1) / 2)), vpool=vpool).clauses)
    # 2 3 1
    # 2 2 2
    # 2 2 2
    # one value per column
    for x in range(n):
        lits = []
        weights = []
        for z in range(1, n + 1):
            for y in range(n):
                lits.append(s(x, y, z))
                weights.append(z)
        p.extend(PBEnc.equals(lits=lits, weights=weights, bound=int((n * (n + 1) / 2)), vpool=vpool).clauses)
    # 3 2 1
    # 2 2 2
    # 1 2 3
    # inequalities hold
    for x in c:
        (a, b) = x        # x1+x2+x3 - (y1+y2+y3) > 0
        (i1, j1) = a      # x1+x2+x3 > y1+y2+y3
        (i2, j2) = b      # X > Y
        lits = []
        weights = []
        for z in range(1, n + 1):
            lits.append(s(i1, j1, z))
            lits.append(s(i2, j2, z))
            weights.append(z)
            weights.append(-z)
        p.extend(PBEnc.atleast(lits=lits, weights=weights, bound=1, vpool=vpool).clauses)
    return p
    # [[2, 1], [-2, -1], [4, 3], [-4, -3], [6, 5], [-6, -5], [8, 7], [-8, -7], [9], [-10, 1], [-11, -5, -1],
    # [-11, 5, 10], [-11, -1, 10], [-12, -2], [-12, 2, 11], [-12, 11], [-13, -2, 11], [-13, 2], [-13, 11],
    # [-14, -6, 12], [-14, 6, 13], [-14, 12, 13], [14], [15], [-16, 3], [-17, -7, -3], [-17, 7, 16],
    # [-17, -3, 16], [-18, -4], [-18, 4, 17], [-18, 17], [-19, -4, 17], [-19, 4], [-19, 17],
    # [-20, -8, 18], [-20, 8, 19], [-20, 18, 19], [20], [21], [-22, 1], [-23, -3, -1],
    # [-23, 3, 22], [-23, -1, 22], [-24, -2], [-24, 2, 23], [-24, 23], [-25, -2, 23],
    # [-25, 2], [-25, 23], [-26, -4, 24], [-26, 4, 25], [-26, 24, 25], [26], [27], [-28, 5],
    # [-29, -7, -5], [-29, 7, 28], [-29, -5, 28], [-30, -6], [-30, 6, 29], [-30, 29], [-31, -6, 29],
    # [-31, 6], [-31, 29], [-32, -8, 30], [-32, 8, 31], [-32, 30, 31], [32], [3], [], [-8]]


def solve(p):
    with MapleChrono(bootstrap_with=p.clauses) as q:
        is_solvable = q.solve()
        if is_solvable:
            print_sol(q.get_model())
        else:
            print("Unsolvable!")


def print_sol(sol):
    print('\n---------------SOLUTION----------------')
    print(sol)
    for i in range(n):
        for j in range(n):
            for k in range(1, n + 1):
                if s(i, j, k) in sol:
                    print(k, end=' ')
        print()


fic = read_file("boards/grid3_1")
v, c = get_grid(fic)
p = get_clause(v, c)
print(p.clauses)
solve(p)

# 1 2 3
# 3 1 2
# 2 3 1

# 2 3 1
# 1 2 3
# 3 1 2

# 2 3 1
# 3 1 2
# 1 2 3

# 2 3 1
# 2 1 3
# 2 2 2