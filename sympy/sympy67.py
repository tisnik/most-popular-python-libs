import sympy as sp

a1 = sp.Array([0]*25)
a2 = a1.reshape(5,5)

print(type(a2))
print()

sp.pprint(a2)
