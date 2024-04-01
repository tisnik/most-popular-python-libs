from toolz import pipe

print(pipe(1, abs, lambda x: x*2))
print(pipe(42, abs, lambda x: x*2))
print(pipe(1000, abs, lambda x: x*2))
