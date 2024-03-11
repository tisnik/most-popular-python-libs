import tiktoken

encoder = tiktoken.get_encoding("cl100k_base")

source_code = '''
    """Ackermannova funkce."""
    if m == 0:
        return n + 1
    if n == 0:
        return A(m - 1, 1)
    return A(m - 1, A(m, n - 1))
'''

tokens = encoder.encode(source_code)
print("Tokens: ", len(tokens))
print(tokens)
