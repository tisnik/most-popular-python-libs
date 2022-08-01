import tokenize

with open("expression.py", "rb") as fin:
    token_generator = tokenize.tokenize(fin.readline)
    for token in token_generator:
        print(token)
