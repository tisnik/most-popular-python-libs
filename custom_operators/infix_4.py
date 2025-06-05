# Vlastní infixové operátory v Pythonu
#
# - třída DotProduct umožňující definici operátoru pro skalární součin
# - odlišné symboly operátoru
# - definice nového operátoru
# - otestování nového operátoru


class DotProduct:

    def __ror__(self, other):
        self.value = other
        return self

    def __or__(self, other):
        dot_product = 0
        for a, b in zip(self.value, other):
            dot_product += a * b
        return dot_product


o = DotProduct()
x = [1, 2, 3]
y = [3, 4, 5]

print(x |o| y)
