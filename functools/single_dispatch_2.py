from functools import singledispatch


@singledispatch
def foo(arg):
    print("Original function foo with argument", arg, "that has type", type(arg))


@foo.register
def _(arg: int):
    print("Integer variant with argument:", arg)


@foo.register
def _(arg: str):
    print("String variant with argument:", arg)


@foo.register
def _(arg: list):
    print("List variant with argument:", arg)


foo(42)
foo("foo")
foo(["foo", "bar", "baz"])
foo(1.4142)
foo(None)
