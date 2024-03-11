import tiktoken

encoder = tiktoken.get_encoding("cl100k_base")

tokens = encoder.encode("Hello world")
print(tokens)

tokens = encoder.encode("hello world")
print(tokens)

tokens = encoder.encode("hello World")
print(tokens)

tokens = encoder.encode("Hello World")
print(tokens)
