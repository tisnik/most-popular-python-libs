# Typové anotace a nástroj Mypy:
# - funkce bez návratové hodnoty s uvedením typových informací
# - zavolání této funkce pro argumenty typu str a int


def message(msg: str) -> None:
    """Funkce s typovými anotacemi."""
    print(f"Zpráva: {msg}")


# zavolání funkce
message("Ahoj")
