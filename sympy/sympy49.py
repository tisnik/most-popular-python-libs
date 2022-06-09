from sympy import symbols, pprint, init_printing
from sympy import Interval, maximum, S

init_printing(use_unicode=True)

x = symbols("x")

f = x ** 3 - 2 * x ** 2

pprint(f)

print()

print(maximum(f, x, Interval(-2, 2)))
print(maximum(f, x, Interval(-1, 1)))
