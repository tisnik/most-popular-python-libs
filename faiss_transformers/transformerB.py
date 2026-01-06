from datasets import load_dataset
from sentence_transformers import SentenceTransformer

import faiss

model = SentenceTransformer("paraphrase-MiniLM-L6-v2")
print(model)

dataset = load_dataset("polygraf-ai/human-sentences-1M-sample-v2", split="train")
print(dataset)

sentences = [sentence for sentence in dataset["text"][0:1000]]
print(f"{len(sentences)} sentences created")

embeddings = model.encode(sentences)
print(f"Embeddings shape: {embeddings.shape}")

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


find_similar_sentences("city", 3)
find_similar_sentences("animal", 3)
find_similar_sentences("geometry", 3)
find_similar_sentences("weather", 3)
find_similar_sentences("game", 3)
find_similar_sentences("school", 3)
