"""Retrieving list size."""

import sys

test_list = []

for i in range(31):
    test_list.append(i)

for i in range(31):
    print(len(test_list), sys.getsizeof(test_list))
    del test_list[-1]
