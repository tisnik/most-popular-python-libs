from typing import Final

x: Final[list[str]] = ["foo", "bar", "baz"]
print(x)

x[1] = "xyzzy"
print(x)
