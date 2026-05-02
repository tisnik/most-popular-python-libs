from typing import Any

from functools import singledispatch


@singledispatch
def function(arg: Any) -> None:
    print("Original function with argument", arg, "that has type", type(arg))


@function.register
def _(arg: int) -> None:
    print("Integer variant with argument:", arg)


@function.register
def _(arg: str) -> None:
    print("String variant with argument:", arg)


@function.register(list)
def _(arg: list[Any]) -> None:
    print("List variant with argument:", arg)


@function.register
def _(arg: None) -> None:
    print("None variant with argument:", arg)


function(42)
function("foo")
function(["foo", "bar", "baz"])
function(1.4142)
function(None)
