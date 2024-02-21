from random import randrange
from toolz.itertoolz import frequencies, unique

values = ("Karel", "Ivan", "Petr", "Pavel", "Jan", "Petr", "Ivan", "Ivan")
print(frequencies(values))
