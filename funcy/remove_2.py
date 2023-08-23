from funcy import lremove


message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
words = message.split()

removed = lremove(lambda word: len(word) > 4, words)
print(removed)
print(list(removed))

print()

removed = lremove(lambda word: len(word) <= 4, words)
print(removed)
print(list(removed))
