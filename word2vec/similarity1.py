import gensim.downloader as downloader

model = downloader.load("word2vec-google-news-300")

print("5 words most similary to 'apple'")
similar = model.most_similar("apple", topn=5)
for word, score in similar:
    print(f"  {word}: {score:.4f}")
print()

print("5 words most similary to 'king'")
both = model.most_similar("king", topn=5)
for word, score in both:
    print(f"  {word}: {score:.4f}")
print()

print("5 words most similary to 'cat'")
both = model.most_similar("cat", topn=5)
for word, score in both:
    print(f"  {word}: {score:.4f}")
print()

print("5 words most similar to 'king' and 'woman'")
result = model.most_similar(positive=["king", "woman"], negative=["man"], topn=5)
for word, score in result:
    print(f"  {word}: {score:.4f}")
