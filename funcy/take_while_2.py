from funcy import takewhile

message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
words = message.split()

filtered = takewhile(lambda x:len(x) > 2, words)

print(filtered)
print(list(filtered))
