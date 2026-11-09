seznam = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

seznam2 = [item * 2 for item in seznam]

seznam3 = [item for item in seznam if item % 3 == 0]

print(seznam)
print(seznam2)
print(seznam3)
