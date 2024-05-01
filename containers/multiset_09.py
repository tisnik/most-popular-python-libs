from multiset import Multiset

m1 = Multiset(["a", "b", "c", "d"])
m2 = Multiset(["c", "d", "e", "f"])

print(m1)
print(m2)
print(m1 | m2)
print(m1 & m2)
print(m1 - m2)
print(m1 ^ m2)
