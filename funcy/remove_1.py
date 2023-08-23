from funcy import remove


message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
words = message.split()

removed = remove(lambda word: len(word) > 4, words)
print(removed)
print(list(removed))

print()

removed = remove(lambda word: len(word) <= 4, words)
print(removed)
print(list(removed))
