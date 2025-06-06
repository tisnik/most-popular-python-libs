# Vlastní infixové operátory v Pythonu
#
# - třída DotProduct umožňující definici operátoru pro skalární součin
# - redefinice speciální metody pro operátor >
# - korektní řešení


class DotProduct:

    def __init__(self):
        self.value = None

    def __gt__(self, other):
        if self.value is None:
            print("<", other)
            self.value = other
            return self

        print(">", other)
        dot_product = 0
        for a, b in zip(self.value, other):
            dot_product += a * b
        return dot_product


o = DotProduct()

x = [1, 2, 3]
y = [3, 4, 5]

print(x <o> y)
