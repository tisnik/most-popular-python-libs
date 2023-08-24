from funcy import split_by

message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
words = message.split()

filtered, rest = split_by(lambda x:len(x) > 2, words)

print(list(filtered))
print(list(rest))
