from pysat.solvers import MapleChrono
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
        return f.read().split('\n')


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
            for z in range(1, n + 1):
                vpool.id('v{0}'.format(s(i, j, z)))
            if v[i][j] != "_":
                p.extend(PBEnc.equals(lits=[s(i, j, v[i][j])], bound=1, vpool=vpool).clauses)
    # one value per square
    for x in range(n):
        for y in range(n):
            lits = []
            for z in range(1, n + 1):
                lits.append(s(x, y, z))
            p.extend(PBEnc.equals(lits=lits, bound=1, vpool=vpool).clauses)
    # unique values in each row or column
    for z in range(1, n + 1):
        for a in range(n):
            lits_row = []
            lits_col = []
            for b in range(n):
                lits_row.append(s(a, b, z))
                lits_col.append(s(b, a, z))
            p.extend(PBEnc.equals(lits=lits_row, bound=1, vpool=vpool).clauses)
            p.extend(PBEnc.equals(lits=lits_col, bound=1, vpool=vpool).clauses)
    # inequalities hold
    # for x in c:
    #     (a, b) = x
    #     (i1, j1) = a
    #     (i2, j2) = b
    #     lits = []
    #     weights = []
    #     for z in range(1, n + 1):
    #         lits.append(s(i1, j1, z)) # greater value
    #         lits.append(s(i2, j2, z)) # lesser value
    #         weights.append(z) # +
    #         weights.append(-z) # -
    #     p.extend(PBEnc.atleast(lits=lits, weights=weights, bound=1, vpool=vpool).clauses)

    for x in c:
        (a, b) = x
        (i1, j1) = a
        (i2, j2) = b
        for y in range(1, n):
            for z in range(y + 1, n + 1):
                p.extend(PBEnc.atleast(lits=[-s(i1, j1, y), -s(i2, j2, z)], bound=1, vpool=vpool).clauses)
    return p


def get_solved_board(solved_model):
    rows = []
    for i in range(n):
        row = []
        for j in range(n):
            for k in range(1, n + 1):
                if s(i, j, k) in solved_model:
                    row.append(str(k))
        rows.append(' '.join(row))
    return '\n'.join(rows)


def solve_with_file(f):
    fic = read_file(f)
    v, c = get_grid(fic)
    p = get_clause(v, c)
    print(p.clauses)
    return solve_with_cnf(p)


def solve_with_cnf(p):
    with MapleChrono(bootstrap_with=p.clauses) as q:
        is_solvable = q.solve()
        if is_solvable:
            print('\n---------------SOLUTION----------------')
            print(get_solved_board(q.get_model()))
            return q.get_model()
        else:
            print("Unsolvable!")
            return None
