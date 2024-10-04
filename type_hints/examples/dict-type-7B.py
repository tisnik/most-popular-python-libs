# Typové anotace a nástroj Mypy:
# - definice slovníku
# - specifikace typu klíčů i typu hodnot
# - hodnoty mohou nabývat None
# - úprava pro Python 3.10

d: dict[str, float | None] = {}

d["foo"] = 1
d["bar"] = 3.14
d["baz"] = None

print(d)
