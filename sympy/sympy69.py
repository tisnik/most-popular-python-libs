import sympy as sp

a1 = sp.ImmutableSparseNDimArray([0] * 25)
a2 = a1.reshape(5, 5)

print(type(a2))
print()

sp.pprint(a2)

a2[(2, 2)] = 42

print()

sp.pprint(a2)
