from mpmath import workdps, mpf, log, sin

x = mpf("0.00")
y = mpf("0.00")

z = log(x)

print("log 0=", z)

inf = mpf("inf")

print("inf+ -inf=", inf+z)
print("inf/inf=", inf/inf)

print("log inf=", log(inf))
print("sin inf=", sin(inf))
