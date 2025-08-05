from sentence_transformers import SentenceTransformer
import faiss
from datasets import load_dataset
from time import time

MODEL_NAME = "paraphrase-MiniLM-L6-v2"
DATASET_ID = "polygraf-ai/human-sentences-1M-sample-v2"


def initialize_model(model_name):
    print("Model initialization started")
    model = SentenceTransformer(model_name)
    print(model)
    print("Model initialization finished")
    return model


def load_dataset_by_id(dataset_id):
    print("Loading dataset started")
    dataset = load_dataset(dataset_id, split="train")
    print("Loading dataset finished")
    return dataset


def build_sentences(dataset, from_, to_):
    print("Building sentences")
    sentences = [sentence for sentence in dataset["text"][from_:to_]]
    print(f"{len(sentences)} sentences created")
    return sentences


def create_embeddings(model, sentences):
    print("Embedding started")
    embeddings = model.encode(sentences)
    print(f"Embeddings shape: {embeddings.shape}")
    print("Embedding finished")
    return embeddings


def create_faiss_index(embeddings):
    print("FAISS index construction started")
    DIMENSIONS = embeddings.shape[1]
    index = faiss.IndexFlatL2(DIMENSIONS)
    index.add(embeddings)
    print(f"Index: {index.ntotal}")
    print("FAISS index construction finished")
    return index


def find_similar_sentences(model, index, query_sentence, k):
    t1 = time()
    query_embedding = model.encode([query_sentence])
    distances, indices = index.search(query_embedding, k)
    print("-"*40)
    print(f"Query: {query_sentence}")
    print(f"Most {k} similar sentences:")
    for i, idx in enumerate(indices[0]):
        print(f"{i + 1}: {sentences[idx]} (Distance: {distances[0][i]})")
    t2 = time()
    print(f"Finished in {t2-t1:3.2} seconds")


model = initialize_model(MODEL_NAME)
dataset = load_dataset_by_id(DATASET_ID)
sentences = build_sentences(dataset, 0, 100000)
embeddings = create_embeddings(model, sentences)
index = create_faiss_index(embeddings)

find_similar_sentences(model, index, "city", 3)
find_similar_sentences(model, index, "animal", 3)
find_similar_sentences(model, index, "geometry", 3)
find_similar_sentences(model, index, "weather", 3)
find_similar_sentences(model, index, "game", 3)
find_similar_sentences(model, index, "school", 3)
