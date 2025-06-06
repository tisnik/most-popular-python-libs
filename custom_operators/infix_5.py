# Vlastní infixové operátory v Pythonu
#
# - třída DotProduct umožňující definici operátoru pro skalární součin
# - pokus o redefinici speciálních metod pro operátory < a >
# - nekorektní řešení!


class DotProduct:

    def __lt__(self, other):
        self.value = other
        return self

    def __gt__(self, other):
        dot_product = 0
        for a, b in zip(self.value, other):
            dot_product += a * b
        return dot_product


o = DotProduct()
x = [1, 2, 3]
y = [3, 4, 5]

print(x <o> y)
