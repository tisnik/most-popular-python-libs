from sympy import symbols, pprint, init_printing
from sympy import Interval, minimum, S

init_printing(use_unicode=True)

x = symbols("x")

f = x ** 3 - 2 * x ** 2

pprint(f)

print()

print(minimum(f, x, Interval(-2, 2)))
print(minimum(f, x, Interval(-1, 1)))
