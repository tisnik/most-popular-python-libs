from funcy import distinct


message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
message *= 3

print(message)

words = message.split()

distilled = distinct(words)
print(distilled)
print(list(distilled))
