import sys

l = []

for i in range(31):
    l.append(i)

for i in range(31):
    print(len(l), sys.getsizeof(l))
    del l[-1]
