from mpmath import mp, mpf

x = mpf("1.00")
y = mpf("7.00")

for digits in range(20):
    mp.dps = digits
    z = x / y
    print(z)
