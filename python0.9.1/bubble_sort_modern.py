import random
import time


def bubble_sort(size):
    a = []
    for i in range(size):
        a.append(random.randint(0, 2**15))
    for i in range(size - 1, 0, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    for i in range(size-1):
        if a[i] > a[i+1]:
            print("FAIL")

t1 = time.time()

bubble_sort(30000)

t2 = time.time()

print("Total time:", t2-t1)
