from mpmath import workdps, mpf, sqrt

x = mpf("2.00")

for digits in range(30):
    with workdps(digits):
        y = sqrt(x)
        print(y)
