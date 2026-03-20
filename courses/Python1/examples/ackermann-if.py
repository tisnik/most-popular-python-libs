# Výpočet Ackermannovy funkce, založeno na konstrukci if

def A(m, n):
    """Ackermannova funkce."""
    if m == 0:
        return n + 1
    if n == 0:
        return A(m - 1, 1)
    return A(m - 1, A(m, n - 1))


# otestování korektnosti výpočtu Ackermannovy funkce
for m in range(4):
    for n in range(5):
        print(m, n, A(m, n))

