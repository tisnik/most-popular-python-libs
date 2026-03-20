from sentence_transformers import SentenceTransformer

model = SentenceTransformer("paraphrase-MiniLM-L6-v2")

print(model)

sentences = [
    "The rain in Spain falls mainly on the plain",
    "The tesselated polygon is a special type of polygon",
    "The quick brown fox jumps over the lazy dog",
    "To be or not to be, that is the question",
    "It is a truth universally acknowledged...",
    "How old are you?",
    "The goat ran down the hill"
]

embeddings = model.encode(sentences)
print(f"Embeddings shape: {embeddings.shape}")

for vector in embeddings:
    print(type(vector), vector.shape)
