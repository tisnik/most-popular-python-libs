from typing import Any

from functools import singledispatchmethod

class BarClass:
    def __init__(self, value: int):
        self.value = value


class FooClass:

    @singledispatchmethod
    def foo(self, arg: Any) -> None:
        print("Original function with argument", arg, "that has type", type(arg))


    @foo.register
    def _(self, arg: int | str) -> None:
        print("Integer or string variant with int or str argument:", arg)


    @foo.register(list | tuple)
    def _(self, arg: list[Any] | tuple[Any, ...]) -> None:
        print("List or tuple variant with argument:", arg)


    @foo.register
    def _(self, arg: BarClass) -> None:
        print("Bar variant with argument:", arg.value)


    @foo.register
    def _(self, arg: None) -> None:
        print("None variant with argument:", arg)


f = FooClass()
f.foo(42)
f.foo("foo")
f.foo(["foo", "bar", "baz"])
f.foo(("foo", "bar", "baz"))
f.foo(BarClass(42))
f.foo(1.4142)
f.foo(None)
