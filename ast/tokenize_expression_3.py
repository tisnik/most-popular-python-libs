import tokenize

with tokenize.open("expression2.py") as fin:
    token_generator = tokenize.generate_tokens(fin.readline)
    for token in token_generator:
        print(token)
