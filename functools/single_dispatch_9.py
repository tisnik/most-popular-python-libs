from typing import Any
import dis

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
    raise Exception("why not")


function(None)


