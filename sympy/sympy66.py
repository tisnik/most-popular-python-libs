import sympy as sp

a1 = sp.Array(range(16))
sp.pprint(a1)
print(a1.rank())
print(a1.shape)

print()

a2 = a1.reshape(2, 2, 2, 2)
sp.pprint(a2)
print(a2.rank())
print(a2.shape)
