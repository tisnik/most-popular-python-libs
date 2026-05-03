from functools import singledispatchmethod


class FooClass:

    @singledispatchmethod
    @staticmethod
    def foo(arg):
        print("Original foo method with argument", arg, "that has type", type(arg))


    @foo.register
    @staticmethod
    def _(arg: int):
        print("Integer variant with argument:", arg)


    @foo.register
    @staticmethod
    def _(arg: str):
        print("String variant with argument:", arg)


    @foo.register
    @staticmethod
    def _(arg: list):
        print("List variant with argument:", arg)


f = FooClass()
f.foo(42)
f.foo("foo")
f.foo(["foo", "bar", "baz"])
f.foo(1.4142)
f.foo(None)
