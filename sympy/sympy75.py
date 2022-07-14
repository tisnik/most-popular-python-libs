import sympy as sp

a = sp.MatrixSymbol("A", 3, 4)
b = sp.MatrixSymbol("B", 4, 3)

sp.pprint(sp.Matrix(a))

print()

sp.pprint(sp.Matrix(b))

print()

c = a * b
sp.pprint(sp.Matrix(c))
