from mpmath import workdps, mp, mpf, sqrt

x = mpf("-2.00")

mp.trap_complex = True

y = sqrt(x)
print(y)
