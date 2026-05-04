from multipledispatch import dispatch

@dispatch(int)
def function(arg: int):
    print("Integer variant with argument:", arg)


@dispatch(int, int)
def function(arg1: int, arg2: int):
    print("Integer variant with two arguments:", arg1, arg2)


@dispatch(str)
def function(arg: str):
    print("String variant with argument:", arg)


@dispatch(str, int)
def function(arg1: str, arg2: int):
    print("String+int variant with arguments:", arg1, arg2)


@dispatch(list)
def function(arg: list):
    print("List variant with argument:", arg)


@dispatch(object)
def function(arg: object):
    print("Original function with argument", arg, "that has type", type(arg))


function(42)
function(42, 0)
function("foo")
function("foo", 42)
function(["foo", "bar", "baz"])
function(1.4142)
function(None)
