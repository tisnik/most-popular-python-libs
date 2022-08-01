import tokenize

with tokenize.open("primes.py") as fin:
    token_generator = tokenize.generate_tokens(fin.readline)
    for token in token_generator:
        print(token)
