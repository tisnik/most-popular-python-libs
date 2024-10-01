# Strukturální pattern matching:
# - komplexní čísla realizovaná formou seznamu dvou hodnot

def test_number(value):
    """Test, o jakou variantu komplexního čísla se jedná."""
    match value:
        case [0, 0]:
            print("Zero")
        case [real, 0]:
            print(f"Real number {real}")
        case [0, imag]:
            print(f"Imaginary number {imag}")
        case [real, imag]:
            print(f"Complex number {real}+i{imag}")
        case _:
            raise ValueError("Not a complex number")


test_number([0,0])
test_number([1,0])
test_number([0,1])
test_number([1,1])
