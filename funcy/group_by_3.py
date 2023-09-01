from funcy import group_by

message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
words = message.split()

grouped = group_by(lambda x:len(x), words)

for key in sorted(grouped.keys()):
    print(key, grouped[key])
