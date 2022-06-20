import sympy as sp

a = sp.MatrixSymbol("A", 3, 4)
print(a)

print()

print(sp.Matrix(a))

print()

sp.pprint(sp.Matrix(a))
