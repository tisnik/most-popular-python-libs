# Compiled Coconut: -----------------------------------------------------------

print(reduce(lambda x, acc: acc * x, range(1, 10)))  #1 (line in Coconut source)

print(list(takewhile(lambda x: x < 10, range(100))))  #3 (line in Coconut source)

print(list(dropwhile(lambda x: x < 10, range(100))))  #5 (line in Coconut source)

print(list(takewhile(lambda x: x < 10, (count()))))  #7 (line in Coconut source)

print(list(takewhile(lambda x: x < 10, (count(0)))))  #9 (line in Coconut source)

print(list(takewhile(lambda x: x < 10, (count(0, 2)))))  #11 (line in Coconut source)
