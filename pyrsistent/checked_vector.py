from pyrsistent import CheckedPVector

class Evens(CheckedPVector):
    __type__ = (int,)
    __invariant__ = lambda n: (n % 2 == 0, "Even")

vector1 = Evens([2, 4, 6])

print(vector1)
print(type(vector1))

vector2 = Evens([1, 2, 3])

print(vector2)
print(type(vector2))
