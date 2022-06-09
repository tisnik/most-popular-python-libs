from sympy import solve, symbols, pprint, init_printing

init_printing(use_unicode=True)

a, b, c, x = symbols("α,β,Γ,x")

f = a * x ** 2 + b * x + c

pprint(f)

solution = solve(f, x)
pprint(solution)
