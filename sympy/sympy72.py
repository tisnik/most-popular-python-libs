import sympy as sp

a1 = sp.ImmutableSparseNDimArray(range(12))
a2 = a1.reshape(3, 4)

sp.pprint(a2)

print()

a3 = a2.transpose()
sp.pprint(a3)
