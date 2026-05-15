from mpmath import mp, mpf

mp.dps = 2

x = mpf("1.00")
y = mpf("3.00")

print("mode\t 1/3\t -1/3")
print("-" * 22)

for rounding in "n", "f", "c", "d", "u":
    mp.rounding = rounding
    z1 = x / y
    z2 = -x / y
    print(rounding, "\t", z1, "\t", z2)
