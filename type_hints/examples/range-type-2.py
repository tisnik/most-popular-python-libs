# Typové anotace a nástroj Mypy:
# - použití datového typu range
# - typ definován pro parametr funkce


def suma(x: range) -> int:
    return sum(x)


print(suma(range(100)))
