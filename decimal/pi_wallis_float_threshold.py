from math import pi

result = 2

n = 1
while True:
    m = 4 * n * n
    u = m / (m-1)
    result *= u

    abs_error = pi - result

    n += 1

    if abs(abs_error) < 0.00000001:
        rel_error = 100.0 * abs_error / pi
        print(result, "\t", abs_error, "\t", rel_error)
        break
