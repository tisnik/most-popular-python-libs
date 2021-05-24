import random

size = 40

a = [random.randrange(0, 20) for i in range(size)]
print(a)

for i in range(size-1, 0, -1):
    print(i)
    for j in range(0, i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print("Sorted")
print(a)
