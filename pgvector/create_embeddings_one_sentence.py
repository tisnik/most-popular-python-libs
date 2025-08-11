from sentence_transformers import SentenceTransformer

model = SentenceTransformer("paraphrase-MiniLM-L6-v2")

print(model)

sentence = "The rain in Spain falls mainly on the plain"

embeddings = model.encode(sentence)
print(f"Embeddings shape: {embeddings.shape}")

vector = embeddings
print(type(vector), vector.shape)
