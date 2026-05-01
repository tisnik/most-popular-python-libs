from functools import singledispatch


@singledispatch
def function(arg):
    print("Original function with argument", arg, "that has type", type(arg))


@function.register
def _(arg: int):
    print("Integer variant with argument:", arg)


@function.register
def _(arg: str):
    print("String variant with argument:", arg)


@function.register
def _(arg: list):
    print("List variant with argument:", arg)


@function.register
def _(arg: None):
    print("None variant with argument:", arg)


function(42)
function("foo")
function(["foo", "bar", "baz"])
function(1.4142)
function(None)
