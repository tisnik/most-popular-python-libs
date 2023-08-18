from funcy import lfilter


message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
words = message.split()

filtered = lfilter(lambda word: len(word) > 4, words)
print(filtered)
print(list(filtered))

print()

filtered = lfilter(lambda word: len(word) <= 4, words)
print(filtered)
print(list(filtered))
