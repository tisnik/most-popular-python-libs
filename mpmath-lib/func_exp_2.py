from mpmath import mpf, workdps

x = mpf("1.2")
y = mpf("2.3")

with workdps(50):
    print("x^y\t", x**y)
