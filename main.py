from pysat.solvers import Solver, MapleChrono
from pysat.formula import CNF

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
    for i in range(n):
        for j in range(n):
            if v[i][j] != "_":
                p.append([s(i, j, v[i][j])])
    # une valeur par case
    for x in range(n):
        for y in range(n):
            ll = []
            for z in range(1, n + 1):
                ll.append(s(x, y, z))
            p.append(ll)
    # une valeur par ligne
    for y in range(n):
        for z in range(1, n + 1):
            for x in range(n - 1):
                for i in range(x + 1, n):
                    p.append([-s(x, y, z), -s(i, y, z)])
    # une valeur par colonne
    for x in range(n):
        for z in range(1, n + 1):
            for y in range(n - 1):
                for i in range(y + 1, n):
                    p.append([-s(x, y, z), -s(x, i, z)])
    # superieur
    for x in c:
        (a, b) = x
        (i1, j1) = a
        (i2, j2) = b
        for y in range(1, n):
            for z in range(y + 1, n + 1):
                p.append([-s(i1, j1, y), -s(i2, j2, z)])
    return p


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


fic = read_file("boards/grid3_fail")
v, c = get_grid(fic)
p = get_clause(v, c)
solve(p)

# 1 2 3
# 3 1 2
# 2 3 1

# 2 3 1
# 1 2 3
# 3 1 2