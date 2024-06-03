# Compiled Coconut: -----------------------------------------------------------

(print)(map(lambda x: x * 2, [1, 2, 3, 4]))  #1 (line in Coconut source)
(print)((list)(map(lambda x: x * 2, [1, 2, 3, 4])))  #2 (line in Coconut source)
(print)(fmap(lambda x: x * 2, [1, 2, 3, 4]))  #3 (line in Coconut source)

print()  #5 (line in Coconut source)

(print)(map(lambda x: x * 2, (1, 2, 3, 4)))  #7 (line in Coconut source)
(print)((list)(map(lambda x: x * 2, (1, 2, 3, 4))))  #8 (line in Coconut source)
(print)(fmap(lambda x: x * 2, (1, 2, 3, 4)))  #9 (line in Coconut source)

print()  #11 (line in Coconut source)

(print)(map(lambda x: x * 2, range(10)))  #13 (line in Coconut source)
(print)((list)(map(lambda x: x * 2, range(10))))  #14 (line in Coconut source)
(print)(fmap(lambda x: x * 2, range(10)))  #15 (line in Coconut source)
