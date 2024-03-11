import tiktoken

encoder = tiktoken.get_encoding("cl100k_base")

spaces = (
        "hello",
        "world",
        "hello world",
        " world",
)

for word in spaces:
    tokens = encoder.encode(word)
    print(f"{word:16}", tokens)
