import sympy as sp

a = sp.MatrixSymbol("A", 3, 4)

sp.pprint(sp.Matrix(a))

print()

sp.pprint(sp.Matrix(a.T))
