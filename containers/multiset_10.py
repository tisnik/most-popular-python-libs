from multiset import Multiset

m1 = Multiset(["a", "a", "b", "b", "c", "c", "d", "d"])
m2 = Multiset(["c", "c", "d", "d", "e", "e", "f", "f"])

print(m1)
print(m2)
print(m1 | m2)
print(m1 & m2)
print(m1 - m2)
print(m1 ^ m2)
