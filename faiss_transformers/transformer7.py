from sentence_transformers import SentenceTransformer
import faiss

model = SentenceTransformer("paraphrase-MiniLM-L6-v2")

print(model)

sentences = [
    "The rain in Spain falls mainly on the plain",
    "The tesselated polygon is a special type of polygon",
    "The quick brown fox jumps over the lazy dog",
    "To be or not to be, that is the question",
    "It is a truth universally acknowledged...",
    "The goat ran down the hill"
]

# Generate embeddings for the sentences
embeddings = model.encode(sentences)
print(f"Embeddings shape: {embeddings.shape}")

similarities = model.similarity(embeddings, embeddings)

DIMENSIONS = embeddings.shape[1]

index = faiss.IndexFlatL2(DIMENSIONS)
index.add(embeddings)

print(f"Index: {index.ntotal}")


def find_similar_sentences(query_sentence, k):
    query_embedding = model.encode([query_sentence])
    distances, indices = index.search(query_embedding, k)
    print("-"*40)
    print(f"Query: {query_sentence}")
    print(f"Most {k} similar sentences:")
    for i, idx in enumerate(indices[0]):
        print(f"{i + 1}: {sentences[idx]} (Distance: {distances[0][i]})")


find_similar_sentences("The quick brown fox jumps over the lazy dog", 3)
find_similar_sentences("quick brown fox jumps over lazy dog", 3)
find_similar_sentences("The quick brown fox jumps over the angry dog", 3)
find_similar_sentences("The quick brown cat jumps over the lazy dog", 3)
