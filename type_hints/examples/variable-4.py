# - specifikace typu lokální proměnné
# - přiřazení nové hodnoty nekompatibilního typu do proměnné


def funkce(param: float) -> int:
    x: int = 1 / param
    return x
