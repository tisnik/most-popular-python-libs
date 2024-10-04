# - definice slovníku
# - specifikace typu klíčů i typu hodnot
# - u klíčů i hodnot je použit typ Union
# - úprava pro Python 3.10

d: dict[int | str, int | float | str] = {}

d["foo"] = 1
d["bar"] = 3.14
d[10] = 10
d[42] = "answer"

print(d)
