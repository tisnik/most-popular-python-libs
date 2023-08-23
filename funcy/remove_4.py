from funcy import lremove


message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
words = message.split()

removed = lremove({"sit"}, words)
print(removed)

removed = lremove({"sit", "sed", "do", "amet"}, words)
print(removed)

removed = lremove({"foo", "sed", "bar"}, words)
print(removed)
