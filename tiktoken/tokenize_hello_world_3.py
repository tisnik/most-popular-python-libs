import tiktoken

encoder = tiktoken.get_encoding("cl100k_base")

tokens = encoder.encode("Hello, world!")
print(tokens)
