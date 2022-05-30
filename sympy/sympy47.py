from sympy import singularities, symbols, pprint
  
a, b, c, d, e, x = symbols('a,b,c,d,e,x')

f = 1/(x**3 - x**2 + x)

pprint(f)

print()

s = singularities(f, x)
pprint(s)
