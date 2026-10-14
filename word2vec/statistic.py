import gensim.downloader as downloader

import enchant
d = enchant.Dict("en_US")

model = downloader.load('word2vec-google-news-300')

print(f"Loaded {len(model)} word vectors, each {model.vector_size}d")

from itertools import combinations
import numpy as np

words = model.index_to_key

best_pair = None
worst_pair = None
best_sim = -1
worst_sim = 1

i = 0
for w1, w2 in combinations(words, 2):
    if d.check(w1) and d.check(w2):
        i += 1
        sim = model.similarity(w1, w2)

        if sim > best_sim:
            best_sim = sim
            best_pair = (w1, w2)

        if sim < worst_sim:
            worst_sim = sim
            worst_pair = (w1, w2)

        if i%10000 == 0:
            print(i, best_pair, best_sim, worst_pair, worst_sim)
