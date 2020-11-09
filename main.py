from pysat.pb import PBEnc
from pysat.solvers import MapleChrono
from pysat.formula import IDPool, CNF
import sys
import re


# 1. Read file characters
# 2. Determine pre-existing cell values and constraints
# 3. Given the pre-existing cell values and constraints, create CNF formula
# 4. Feed that CNF formula into SAT solver

# s : int x, int y, string/int z -> int output
# assigns a unique number to represent the boolean variable for a particular
# value z in tile position (x, y)
def s(x, y, z):
    if z == "_":
        z = 0
    return (n * n) * x + n * y + int(z)


# read_file : string file_name -> list output
# given a file path and name, return the characters of the corresponding file
# split into a list that contains each line of the file as a separate string
# throws FileNotFoundError if input file_name cannot be found
def read_file(file_name):
    try:
        with open(file_name, 'r') as f:
            return f.read().split('\n')
    except FileNotFoundError:
        print("Invalid file path given!")
        sys.exit(1)


# get_grid : list f -> list v, list c outputs
# given a list of the rows of a Futoshiki board in string format,
# return the list v containing the pre-existing tile values
# on the board and also return the list c which contains
# pairs representing the constraints/inequalities in the board,
# with the first element in the pair being larger than the second
def get_grid(f):
    global n

    def h(i, j):
        return (i // 2), (j // 2)

    v, c, n = [], [], (len(f) + 1) // 2

    for i in range(len(f)):
        if i % 2 == 0:
            ll = []
            for j in range(len(f[i])):
                if f[i][j] == '<':
                    c.append([h(i, j + 1), h(i, j - 1)])
                elif f[i][j] == '>':
                    c.append([h(i, j - 1), h(i, j + 1)])
                elif f[i][j] != ' ':
                    ll.append(f[i][j])
            v.append(ll)
        else:
            for j in range(len(f[i])):
                if f[i][j] == '^':
                    c.append([h(i + 1, j), h(i - 1, j)])
                if f[i][j] == 'v' or f[i][j] == 'V':
                    c.append([h(i - 1, j), h(i + 1, j)])
    return v, c


# get_clause : list v, list c -> CNF clauses p output
# given two lists describing a Futoshiki board:
# v (already assigned variables) and c (tile constraints),
# return the CNF encoding of the Futoshiki board
def get_clause(v, c):
    p = CNF()
    vpool = IDPool()
    # add numbers that are prefilled and add all boolean variables to the pool of used variables
    for i in range(n):
        for j in range(n):
            for z in range(1, n + 1):
                vpool.id('v{0}'.format(s(i, j, z)))
            if v[i][j] != "_":
                p.extend(PBEnc.equals(lits=[s(i, j, v[i][j])], bound=1, vpool=vpool).clauses)
    # ensure there is at least one value per square
    for x in range(n):
        for y in range(n):
            lits = list(map(lambda z: s(x, y, z), range(1, n + 1)))
            p.extend(PBEnc.atleast(lits=lits, bound=1, vpool=vpool).clauses)
    # ensure there exists only 1 of each value in each row and column
    for z in range(1, n + 1):
        for a in range(n):
            lits_row = list(map(lambda b: s(a, b, z), range(n)))
            lits_col = list(map(lambda b: s(b, a, z), range(n)))
            p.extend(PBEnc.equals(lits=lits_row, bound=1, vpool=vpool).clauses)
            p.extend(PBEnc.equals(lits=lits_col, bound=1, vpool=vpool).clauses)
    # ensure inequalities hold
    for x in c:
        (a, b) = x
        (i1, j1) = a
        (i2, j2) = b
        lits = list(map(lambda z: s(i1, j1, z), range(1, n + 1))) + \
               list(map(lambda z: s(i2, j2, z), range(1, n + 1)))
        weights = list(range(1, n + 1)) + list(range(-1, -n - 1, -1))
        p.extend(PBEnc.atleast(lits=lits, weights=weights, bound=1, vpool=vpool).clauses)
    return p


# get_solved_board : Model solved_model, list board -> list board
# given the solved model of a board as well as the list of the board's rows as strings,
# return the solved board as a single string
def get_solved_board(solved_model, board):
    board = re.sub('[0-9]', '_', '\n'.join(board))
    for i in range(n):
        for j in range(n):
            next_to_replace = board.find('_')
            for k in range(1, n + 1):
                if s(i, j, k) in solved_model:
                    board = board[:next_to_replace] + str(k) + board[next_to_replace + 1:]
    return board


# solve_with_file : string f -> Model output
# given a file path to a Futoshiki board, return the solved model and prints out a solution if
# the file exists, if the file contains a Futoshiki board, and if there exists a solution.
# if the file does not exist or the board is unsolvable, the user is notified accordingly.
def solve_with_file(f):
    board = read_file(f)
    v, c = get_grid(board)
    p = get_clause(v, c)
    with MapleChrono(bootstrap_with=p.clauses) as q:
        is_solvable = q.solve()
        if is_solvable:
            print('---------------SOLUTION----------------')
            print(get_solved_board(q.get_model(), board))
            return q.get_model()
        else:
            print("Unsolvable!")
            return None


# running the solver from the terminal where the singular command line argument is
# the file where the desired board-to-be-solved is stored
if __name__ == "__main__":
    solve_with_file(sys.argv[1])
