from typing import Any, Callable


def log_calc(function: Callable[..., Any], *args: Any) -> Any:
    function_name = getattr(function, '__name__', repr(function))
    print()
    print(f"Called with {function_name} with args={args}")
    result = function(*args)
    print(f"Evaluated result: {result}")
    return result


def add(x: int, y: int) -> int:
    return x + y


def mul(x: int, y: int) -> int:
    return x * y


def less_than(x: int, y: int) -> bool:
    return x < y


print(log_calc(min, 10, 20))
print(log_calc(max, 10, 20))
print(log_calc(id, 42))
print(log_calc(add, 10, 20))
print(log_calc(mul, 6, 7))
print(log_calc(less_than, 10, 20))
