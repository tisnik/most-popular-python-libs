import gensim.downloader as downloader

model = downloader.load("word2vec-google-news-300")

print("5 words most similar to 'king' and 'woman'")
result = model.most_similar(positive=["king", "woman"], negative=["man"], topn=5)
for word, score in result:
    print(f"  {word}: {score:.4f}")
