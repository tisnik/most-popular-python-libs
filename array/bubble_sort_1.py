import random
from time import perf_counter

size = 10000

a = [random.randrange(0, 10000) for i in range(size)]

t1 = perf_counter()

for i in range(size - 1, 0, -1):
    for j in range(0, i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

t2 = perf_counter()

print(f"Sorted in {t2-t1} seconds:")

print("\nBegins with:")
print(a[:100])

print("\nEnds with:")
print(a[-100:])
