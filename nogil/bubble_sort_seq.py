from time import perf_counter
import random

def bubble_sort(size):
    a = [random.randrange(0, 10000) for i in range(size)]

    t1 = perf_counter()

    for i in range(size - 1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    t2 = perf_counter()

    print(f"Sorted in {t2-t1} seconds:")


t1 = perf_counter()

for i in range(100):
    bubble_sort(5000)

t2 = perf_counter()

print(f"Total time: {t2-t1} seconds:")
