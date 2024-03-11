import tiktoken

encoder = tiktoken.get_encoding("cl100k_base")

compound_words = (
        "fire",
        "fox",
        "place",
        "fireplace",
        "firefox",
)

for word in compound_words:
    tokens = encoder.encode(word)
    print(f"{word:12}", tokens)
