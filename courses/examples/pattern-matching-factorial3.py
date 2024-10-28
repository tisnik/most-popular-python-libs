# Strukturální pattern matching:
# - výpočet faktoriálu s využitím pattern matchingu
# - test, zda má vstup korektní typ


def factorial(n):
    """Rekurzivní výpočet faktoriálu."""
    match n:
        case 0:
            return 1
        case 1:
            return 1
        case x if isinstance(x, int) and x>1:
            return x * factorial(x-1)
        case _:
            raise TypeError("expecting integer >= 0")


# tisk tabulky faktoriálů
for i in range(-1, 10):
    try:
        print(i, factorial(i))
    except Exception as e:
        print(e)

# test reakce na nekorektní vstup
try:
    print(factorial(3.14))
except Exception as e:
    print(e)

# test reakce na nekorektní vstup
try:
    print(factorial("hello"))
except Exception as e:
    print(e)
