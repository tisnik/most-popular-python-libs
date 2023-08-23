from funcy import lfilter


message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
words = message.split()

filtered = lfilter("et", words)
print(filtered)

filtered = lfilter("a", words)
print(filtered)

filtered = lfilter("o", words)
print(filtered)

filtered = lfilter("or$", words)
print(filtered)
