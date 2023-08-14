from funcy import rcurry


def pow(x, y):
    return x ** y


n_pow = rcurry(pow)
pow2 = n_pow(2)
pow10 = n_pow(10)

print(pow2(2))
print(pow10(2))
