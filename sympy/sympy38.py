from sympy import diff, symbols, pprint
  
x = symbols('x')

f = 5*x**3 + 4*x**2 + 3*x + 4 + 1/x

pprint(f)

print()

diff1 = diff(f, x)
pprint(diff1)
