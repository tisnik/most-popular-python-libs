# Strukturální pattern matching:
# - výpočet faktoriálu s využitím pattern matchingu
# - základní varianta akceptující neplatné vstupy

def factorial(n):
    """Rekurzivní výpočet faktoriálu."""
    match n:
        case 0:
            return 1
        case 1:
            return 1
        case x:
            return x * factorial(x-1)


# tisk tabulky faktoriálů
for i in range(0, 10):
    print(i, factorial(i))
