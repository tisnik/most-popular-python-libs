from multipledispatch import dispatch

@dispatch(int)
def function(arg: int):
    print("Integer variant with argument:", arg)


@dispatch(str)
def function(arg: str):
    print("String variant with argument:", arg)


@dispatch(list)
def function(arg: list):
    print("List variant with argument:", arg)


@dispatch(object)
def function(arg: object):
    print("Original function with argument", arg, "that has type", type(arg))


function(42)
function("foo")
function(["foo", "bar", "baz"])
function(1.4142)
function(None)
