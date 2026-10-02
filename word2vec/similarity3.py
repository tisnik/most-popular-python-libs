import gensim.downloader as downloader

model = downloader.load("word2vec-google-news-300")

result = model.most_similar(positive=["king", "woman"], negative=["man"], topn=3)
print("king - man + woman = ")
for word, score in result:
    print(f"  {word}: {score:.4f}")

result = model.most_similar(positive=["prince", "adult"], negative=["young"], topn=3)
print("prince - young + adult = ")
for word, score in result:
    print(f"  {word}: {score:.4f}")

result = model.most_similar(positive=["cat", "young"], negative=["old"], topn=3)
print("cat - old + young = ")
for word, score in result:
    print(f"  {word}: {score:.4f}")
