from sympy import pprint, solve, Symbol
from sympy.physics.units import meter, second, kelvin

a = Symbol("a") * meter
b = Symbol("b") * second
c = Symbol("c") * kelvin

x = Symbol("x")

f = a * x ** 2 + b * x + c

pprint(f)
print()

solution = solve(f, x)
pprint(solution)
