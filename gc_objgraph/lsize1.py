import sys

l = []

for i in range(31):
    print(len(l), sys.getsizeof(l))
    l.append(i)
