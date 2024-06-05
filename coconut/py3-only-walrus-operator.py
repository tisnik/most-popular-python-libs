# Compiled Coconut: -----------------------------------------------------------

values = (1, 2, 3, 4, 5)  #1 (line in Coconut source)

result = _coconut.dict((("count", (count := len(values))), ("sum", (summ := sum(values))), ("mean", summ / count)))  #3 (line in Coconut source)

print(result)  #9 (line in Coconut source)
