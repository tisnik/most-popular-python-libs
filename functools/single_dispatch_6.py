from typing import Any

from functools import singledispatch


@singledispatch
def function(arg: Any, second: int) -> None:
    print("Original function with argument", arg, "that has type", type(arg))


@function.register
def _(arg: int, second: int) -> None:
    print("Integer variant with argument:", arg)


@function.register
def _(arg: str, second: int) -> None:
    print("String variant with argument:", arg)


@function.register(list)
def _(arg: list[Any], second: int) -> None:
    print("List variant with argument:", arg)


@function.register
def _(arg: None, second: int) -> None:
    print("None variant with argument:", arg)


function(42, 0)
function("foo", 0)
function(["foo", "bar", "baz"], 0)
function(1.4142, 0)
function(None, 0)
