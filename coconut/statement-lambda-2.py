# Compiled Coconut: -----------------------------------------------------------

message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"  #1 (line in Coconut source)
words = message.split()  #2 (line in Coconut source)

def _coconut_lambda_0(word):  #4 (line in Coconut source)
    length = len(word)  #4 (line in Coconut source)
    return length > 4  #4 (line in Coconut source)

filtered = filter((_coconut_lambda_0), words)  #4 (line in Coconut source)

for word in filtered:  #6 (line in Coconut source)
    print(word)  #7 (line in Coconut source)
