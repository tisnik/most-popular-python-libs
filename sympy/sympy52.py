from sympy import symbols, pprint, init_printing
from sympy import Interval, is_increasing, oo

init_printing(use_unicode=True)

x = symbols('x')

f = x**3 - 2*x**2

pprint(f)

print()

i1 = Interval(-oo, 2)
i2 = Interval(-oo, 0)
i3 = Interval(0, 1)
i4 = Interval(1.5, oo)

print(i1, is_increasing(f, i1, x))
print(i2, is_increasing(f, i2, x))
print(i3, is_increasing(f, i3, x))
print(i4, is_increasing(f, i4, x))
