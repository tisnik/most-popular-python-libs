from sympy import integrate, symbols, pprint

a, b, x = symbols("a,b,x")

f = a * x + b

pprint(f)

solution = integrate(f, x)
pprint(solution)
