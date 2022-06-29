l = []

list1 = [1, "foo", (1, 2, 3), l]
print(list1)
print(type(list1))

l.append(1)
print(list1)
print(type(list1))

l.append(2)
print(list1)
print(type(list1))

l = []
print(list1)
print(type(list1))
