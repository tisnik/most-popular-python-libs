class Foo:
    def __init__(self, value):
        self._value = value

    def __add__(self, other):
        return Foo(self._value + other._value)

    def __str__(self):
        return "*" * self._value


def test_adding():
    f1 = Foo(1)
    f2 = Foo(2)

    print(f1 + f2)
