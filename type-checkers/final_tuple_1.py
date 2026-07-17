from typing import Final

x: Final[tuple[str, ...]] = ("foo", "bar", "baz")
print(x)

x = ("x", "y", "z")
print(x)
