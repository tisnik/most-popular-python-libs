from typing import Final

x: Final[tuple[str, ...]] = ("foo", "bar", "baz")
print(x)

x.append("xyzzy")
print(x)
