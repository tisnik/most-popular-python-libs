from mpmath import pi, mpf, mp

mp.dps = 100

result = mpf("2")

for n in range(1, 1000):
    m = mpf(4 * n * n)
    u = m / (m-1)
    result *= u

    abs_error = pi - result
    rel_error = mpf("100.0") * abs_error / pi
    print(result, "\t", abs_error, "\t", rel_error)
