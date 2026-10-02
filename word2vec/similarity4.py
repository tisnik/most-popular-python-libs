import gensim.downloader as downloader

model = downloader.load('word2vec-google-news-300')

print("Cosine similarity between two specific words")

sim = model.similarity("day", "night")
print(f"Similarity between 'day' and 'night': {sim:.4f}")

sim2 = model.similarity("day", "car")
print(f"Similarity between 'day' and 'car': {sim2:.4f}")

sim3 = model.similarity("apple", "orange")
print(f"Similarity between 'apple' and 'orange': {sim3:.4f}")

sim4 = model.similarity("apple", "pear")
print(f"Similarity between 'apple' and 'pear': {sim4:.4f}")

sim5 = model.similarity("cat", "kitty")
print(f"Similarity between 'cat' and 'kitty': {sim5:.4f}")

sim6 = model.similarity("cat", "tree")
print(f"Similarity between 'cat' and 'tree': {sim6:.4f}")

sim7 = model.similarity("while", "occur")
print(f"Similarity between 'while' and 'occur': {sim7:.4f}")
