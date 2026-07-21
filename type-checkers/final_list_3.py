from typing import Final

x: Final[list[str]] = ["foo", "bar", "baz"]
print(x)

x.append("xyzzy")
print(x)
