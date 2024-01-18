from sympy import Interval, init_printing, maximum, pprint, symbols

init_printing(use_unicode=True)

x = symbols("x")

f = x ** 3 - 2 * x ** 2

pprint(f)

print()

print(maximum(f, x, Interval(-2, 2)))
print(maximum(f, x, Interval(-1, 1)))
