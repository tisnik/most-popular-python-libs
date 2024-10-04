# Typové anotace a nástroj Mypy:
# - použití datového typu range
# - typ definován pro návratovou hodnotu funkce


def funkce(from_val: int, to_val: int) -> range:
    return range(from_val, to_val)
