import tiktoken

encoder = tiktoken.get_encoding("cl100k_base")

compound_words = (
        "unprofessionally",
        "internationalization",
        "counterrevolutionaries",
)

for word in compound_words:
    tokens = encoder.encode(word)
    print(f"{word:22}", tokens)
