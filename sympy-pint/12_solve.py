from sympy import Symbol, pprint, solve
from sympy.physics.units import meter, second

a = Symbol("a") * meter
b = Symbol("b") * meter
c = Symbol("c") * meter

x = Symbol("x")

f = a * x ** 2 + b * x + c

pprint(f)
print()

solution = solve(f, x)
pprint(solution)
