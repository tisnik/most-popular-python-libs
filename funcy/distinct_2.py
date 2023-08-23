from funcy import ldistinct


message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
message *= 3

print(message)

words = message.split()

distilled = ldistinct(words)
print(distilled)
print(list(distilled))
