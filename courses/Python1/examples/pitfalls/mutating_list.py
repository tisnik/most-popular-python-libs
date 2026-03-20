numbers = [n for n in range(10)]

print(numbers)

for i in range(len(numbers)):
    print(i)
    if numbers[i] % 2 == 0:
        del numbers[i]

print(numbers)
