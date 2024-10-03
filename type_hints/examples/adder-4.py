# Typové anotace a nástroj Mypy:
# - funkce s uvedením typových informací
# - zavolání této funkce pro různé typy argumentů


def add(a: int, b: int) -> int:
    """Funkce s typovými anotacemi."""
    return a + b


# zavolání funkce add s argumenty různých typů
print(add(1, 2))
print(add(1.1, 2.2))
print(add(1 + 1j, 2 + 2j))
print(add("foo", "bar"))
print(add([1, 2, 3], [4, 5, 6]))
print(add((1, 2, 3), (4, 5, 6)))
