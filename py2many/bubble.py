def bubble_sort(size):
    a = [random.randrange(0, 10000) for i in range(size)]

    for i in range(size - 1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    print(a)
