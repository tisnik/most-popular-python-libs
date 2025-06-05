# Vlastní infixové operátory v Pythonu
#
# - třída HackyMul umožňující definici operátoru typu <<x>> apod.
# - bez výpisu ladicích informací
# - výpočet tabulky malé násobilky přes nový "operátor"


class HackyMul:

    def __rlshift__(self, other):
        self.value = other
        return self

    def __rshift__(self, other):
        return self.value * other


x = HackyMul()

for j in range(1, 11):
    for i in range(1, 11):
        r = i <<x>> j
        print(f"{r:3d}", end=" ")
    print()
