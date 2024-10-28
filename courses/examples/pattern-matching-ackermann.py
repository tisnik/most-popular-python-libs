# Strukturální pattern matching:
# - Výpočet Ackermannovy funkce

def A(m, n):
    """Ackermannova funkce."""
    match (m, n):
        case (0, n):
            return n + 1
        case (m, 0):
            return A(m-1, 1)
        case (m, n):
            return A(m - 1, A(m, n - 1))


# otestování korektnosti výpočtu Ackermannovy funkce
for m in range(4):
    for n in range(5):
        print(m, n, A(m, n))

