# Compiled Coconut: -----------------------------------------------------------

import random  #1 (line in Coconut source)

message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"  #3 (line in Coconut source)
words = message.split()  #4 (line in Coconut source)

filtered = filter(lambda _=None: random.random() > 0.5, words)  #6 (line in Coconut source)

for word in filtered:  #8 (line in Coconut source)
    print(word)  #9 (line in Coconut source)
