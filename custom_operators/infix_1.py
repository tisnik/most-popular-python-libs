# Vlastní infixové operátory v Pythonu
#
# - třída HackyMul umožňující definici operátoru typu <<x>> apod.
# - při volání speciálních metod se vypisují ladicí informace


class HackyMul:

    def __rlshift__(self, other):
        print("rlshift:", other)
        self.value = other
        return self

    def __rshift__(self, other):
        print("rshift: ", other)
        return self.value * other


x = HackyMul()
print(2 <<x>> 3)

y = HackyMul()
print(3 <<y>> 3)

z = HackyMul()
i = 10
j = 20
print(i <<z>> j)
