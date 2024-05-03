from sympy import Symbol, pprint, solve
from sympy.physics.units import kelvin, meter, second

a = Symbol("a") * meter
b = Symbol("b") * second
c = Symbol("c") * kelvin

x = Symbol("x")

f = a * x ** 2 + b * x + c

pprint(f)
print()

solution = solve(f, x)
pprint(solution)
