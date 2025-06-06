# Vlastní infixové operátory v Pythonu
#
# - třída Infix umožňující definici jakéhokoli binárního operátoru
# - definice několika operátorů
# - otestování nových operátorů


class Infix:
    def __init__(self, function):
        self.function = function

    def __rlshift__(self, other):
        # uzávěr
        return Infix(lambda x, self=self, other=other: self.function(other, x))

    def __rshift__(self, other):
        # levá hodnota je již dostupná v uzávěru
        return self.function(other)

    def __ror__(self, other):
        return self.__rlshift__(other)

    def __or__(self, other):
        return self.__rshift__(other)


# operátor součinu
print("multiply:")

x=Infix(lambda x,y: x*y)
print(2 |x| 4)

print("-" * 20)

# operátor testu typu hodnoty
print("'is a' and 'instance of':")
isa=Infix(lambda x,y: x.__class__==y.__class__)
print([1,2,3] |isa| [])

# operátor testu, zda je hodnota instancí třídy
instance_of=Infix(lambda x,y: isinstance(x, y))
print(1 |instance_of| int)
print(1 |instance_of| str)
print("foo" |instance_of| str)

print(1 |instance_of| int and "foo" |instance_of| str)

print("-" * 20)

print("has attr:")
has_attr=Infix(lambda x,y: hasattr(x, y))
print(str |has_attr| "tolower")
print(str |has_attr| "tolowercase")
print(str |has_attr| "lower")
print(str |has_attr| "__doc__")

print("-" * 20)

print("has method:")
has_method=Infix(lambda x,y: hasattr(x, y) and callable(getattr(x, y, None)))
print(str |has_method| "tolower")
print(str |has_method| "tolowercase")
print(str |has_method| "lower")
print(str |has_method| "__doc__")

print("-" * 20)

print("is in:")
is_in=Infix(lambda x,y: x in y)
print(1 |is_in| {1:'one'})
print(1 |is_in| {1:'one'})

print("-" * 20)

print("gcd:")

import math
gcd=Infix(lambda x,y: math.gcd(x, y))
print(12 |gcd| 8)


print("div:")

import operator
div=Infix(operator.floordiv)
print(10 |div| (4 |div| 2))
