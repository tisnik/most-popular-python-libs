from decimal import Decimal
from math import pi

result = Decimal(2)

for n in range(1, 1000):
    m = Decimal(4 * n * n)
    u = m / (m-1)
    result *= u

    abs_error = Decimal(pi) - result
    rel_error = Decimal(100.0) * abs_error / Decimal(pi)
    print(result, "\t", abs_error, "\t", rel_error)
