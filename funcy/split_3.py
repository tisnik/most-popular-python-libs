from funcy import split

message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
words = message.split()

selected, unselected = split(lambda x:len(x) > 5, words)

print(list(selected))
print(list(unselected))
