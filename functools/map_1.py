message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
words = message.split()

lengths = map(len, words)
print(list(lengths))
