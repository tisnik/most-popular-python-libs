import sys

test_list = []

for i in range(31):
    print(len(test_list), sys.getsizeof(test_list))
    test_list.append(i)
