import sympy as sp

a1 = sp.Array(range(16))
sp.pprint(a1)

print()

a2 = a1.reshape(2,8)
sp.pprint(a2)

print()

a3 = a1.reshape(4,4)
sp.pprint(a3)

print()

a4 = a1.reshape(4,2,2)
sp.pprint(a4)

print()

a5 = a1.reshape(2,4,2)
sp.pprint(a5)

print()

a6 = a1.reshape(2,2,4)
sp.pprint(a6)

print()

