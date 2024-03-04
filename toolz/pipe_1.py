from toolz import pipe


print(pipe(1, str, len))
print(pipe(42, str, len))
print(pipe(1000, str, len))
