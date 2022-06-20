import sympy as sp

a1 = sp.ImmutableSparseNDimArray(range(12))
a2 = a1.reshape(3,4)

sp.pprint(a2)

print()

a3 = 2*a2
sp.pprint(a3)

print()

a4 = a2 + a3
sp.pprint(a4)
