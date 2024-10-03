# - funkce s uvedením typových informací pro dvě varianty argumentů
# - použití dekorátoru @overload
# - zavolání této funkce pro různé typy argumentů


from typing import Union, overload


@overload
def add(a: int, b: int) -> int:
    ...


@overload
def add(a: str, b: str) -> str:
    ...


def add(a: Union[int, str], b: Union[int, str]) -> Union[int, str]:
    """Funkce s typovými anotacemi."""
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + b
    else:
        raise TypeError("Mixing int and str is not supported!")


# zavolání funkce add s argumenty různých typů
print(add(1, 2))
print(add("foo", "bar"))
print(add(1, "bar"))
print(add("foo", 2))
