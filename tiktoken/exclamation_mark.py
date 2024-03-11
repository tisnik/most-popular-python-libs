import tiktoken

encoder = tiktoken.get_encoding("cl100k_base")

tokens = encoder.encode("!")
print(tokens)
