from decimal import Decimal
from math import pi

result = Decimal(2)

n = Decimal(1)

while True:
    m = Decimal(4 * n * n)
    u = m / (m-1)
    result *= u

    abs_error = Decimal(pi) - result
    n += 1

    if abs(abs_error) < 0.00000001:
        rel_error = Decimal(100.0) * abs_error / Decimal(pi)
        print(result, "\t", abs_error, "\t", rel_error)
        break
