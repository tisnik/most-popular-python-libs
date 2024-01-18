from sympy import Interval, init_printing, minimum, pprint, symbols

init_printing(use_unicode=True)

x = symbols("x")

f = x ** 3 - 2 * x ** 2

pprint(f)

print()

print(minimum(f, x, Interval(-2, 2)))
print(minimum(f, x, Interval(-1, 1)))
