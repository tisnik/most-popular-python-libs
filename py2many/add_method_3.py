class Foo:
    def __init__(self, value: int):
        self._value = value

    def __add__(self, other: Foo) -> Foo:
        return Foo(self._value + other._value)

    def __str__(self) -> str:
        return "*" * self._value
