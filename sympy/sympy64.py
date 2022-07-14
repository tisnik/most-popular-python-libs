import sympy as sp

a = sp.Array(range(12), (4, 3))

sp.pprint(a)
print(a.rank())
print(a.shape)
