message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
words = message.split()

filtered = [word for word in words if len(word) > 4]
print(list(filtered))

filtered = [word for word in words if len(word) <= 4]
print(list(filtered))
