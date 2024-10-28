# Strukturální pattern matching:
# - Výpočet Fibonacciho posloupnost realizovaný s využitím
#   pattern matchingu


def fib(value):
    """Výpočet jednoho prvku Fibonacciho posloupnosti."""
    match value:
        case 0:
            return 0
        case 1:
            return 1
        case n if n>1:
            return fib(n-1) + fib(n-2)
        case _ as wrong:
            raise ValueError("Wrong input", wrong)


# tisk tabulky s prvky Fibonacciho posloupnosti
for n in range(0, 11):
    print(n, fib(n))

# test neplatného vstupu
fib(-1)
