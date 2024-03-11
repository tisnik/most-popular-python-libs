import tiktoken

encoder = tiktoken.get_encoding("cl100k_base")

compound_words = (
        "inter",
        "intermedial",
        "intermediate",
        "intermediaries",
        "intermediation",
)

for word in compound_words:
    tokens = encoder.encode(word)
    print(f"{word:14}", tokens)
