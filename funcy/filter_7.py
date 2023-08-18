from funcy import lfilter


message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
message *= 3

print(message)

words = message.split()

filtered = lfilter({"sit"}, words)
print(filtered)

filtered = lfilter({"sit", "sed", "do"}, words)
print(filtered)

filtered = lfilter({"foo", "sed", "bar"}, words)
print(filtered)
