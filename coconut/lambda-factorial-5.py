# Compiled Coconut: -----------------------------------------------------------

n = range(0, 11)  #1 (line in Coconut source)

factorials = map(lambda n: reduce(lambda a, b: a * b, range(1, n + 1), 1), n)  #3 (line in Coconut source)

(print)((list)(factorials))  #5 (line in Coconut source)
