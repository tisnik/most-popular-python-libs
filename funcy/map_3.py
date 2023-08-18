from funcy import lmap

message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
words = message.split()

lengths = lmap(len, words)

print(lengths)
print(list(lengths))
