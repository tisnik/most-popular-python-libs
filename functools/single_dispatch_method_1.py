from functools import singledispatchmethod


class FooClass:

    @singledispatchmethod
    def foo(self, arg):
        print("Original foo method with argument", arg, "that has type", type(arg))


    @foo.register
    def _(self, arg: int):
        print("Integer variant with argument:", arg)


    @foo.register
    def _(self, arg: str):
        print("String variant with argument:", arg)


    @foo.register
    def _(self, arg: list):
        print("List variant with argument:", arg)


f = FooClass()
f.foo(42)
f.foo("foo")
f.foo(["foo", "bar", "baz"])
f.foo(1.4142)
f.foo(None)
