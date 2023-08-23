from funcy import lremove


message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
words = message.split()

removed = lremove("et", words)
print(removed)

removed = lremove("a", words)
print(removed)

removed = lremove("o", words)
print(removed)
