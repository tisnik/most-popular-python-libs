from multipledispatch import dispatch

@dispatch(int, int, int)
def function(arg1: int, arg2: int, arg3: int):
    print("Variant [int, int, int]")

@dispatch(str, int, int)
def function(arg1: str, arg2: int, arg3: int):
    print("Variant [str, int, int]")

@dispatch(int, str, int)
def function(arg1: int, arg2: str, arg3: int):
    print("Variant [int, str, int]")

@dispatch(int, int, str)
def function(arg1: int, arg2: int, arg3: str):
    print("Variant [int, int, str]")




function(1, 2, 3)
function("foo", 2, 3)
function(1, "bar", 3)
function(1, 2, "baz")
function("foo", 2, "baz")
