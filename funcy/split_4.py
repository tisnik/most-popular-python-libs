from funcy import lsplit

message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
words = message.split()

selected, unselected = lsplit(lambda x:len(x) > 5, words)

print(selected)
print(unselected)
