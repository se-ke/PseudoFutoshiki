from pysat.solvers import Solver, MapleChrono
from pysat.formula import CNF

testFormula = CNF()

testFormula.append([-1, 2])
testFormula.append([-2, 3])
# p xor p
# p and not p
# p iff not p


with MapleChrono(bootstrap_with=testFormula.clauses) as m:
    print(m.solve())
#(¬𝑥1∨𝑥2)∧(¬𝑥2∨𝑥3).

# (!a or b) and (a or !b) and (!a or !b) and (a or b)

