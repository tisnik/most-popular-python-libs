import sympy as sp

a = sp.MatrixSymbol("A", 2, 2)

sp.pprint(sp.Matrix(a))

print()

sp.pprint(sp.Matrix(a.I))
