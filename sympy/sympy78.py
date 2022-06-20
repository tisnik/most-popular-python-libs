import sympy as sp

a = sp.MatrixSymbol("A", 2, 2)
b = sp.MatrixSymbol("B", 2, 2)

c = a*b

sp.pprint(sp.Matrix(c))

print()

sp.pprint(sp.Matrix(c.I))
