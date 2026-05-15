from mpmath import workdps, mpf

x = mpf("1.00")
y = mpf("7.00")

for digits in range(20):
    with workdps(digits):
        z = x / y
        print(z)
