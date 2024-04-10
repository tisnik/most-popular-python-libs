from decimal import Decimal, getcontext
from decimal import (
    ROUND_CEILING,
    ROUND_DOWN,
    ROUND_FLOOR,
    ROUND_HALF_DOWN,
    ROUND_HALF_EVEN,
    ROUND_HALF_UP,
    ROUND_UP,
    ROUND_05UP,
)

x = Decimal(1)
y = Decimal(7)


roundings = (
    ROUND_CEILING,
    ROUND_DOWN,
    ROUND_FLOOR,
    ROUND_HALF_DOWN,
    ROUND_HALF_EVEN,
    ROUND_HALF_UP,
    ROUND_UP,
    ROUND_05UP,
)

for round_mode in roundings:
    getcontext().rounding = round_mode
    print(round_mode)
    for i in range(1, 10):
        z = (x / y).quantize(Decimal(10) ** -i)
        print(z)
    print()
