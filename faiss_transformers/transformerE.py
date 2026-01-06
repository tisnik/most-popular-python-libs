from time import time

from datasets import load_dataset
from sentence_transformers import SentenceTransformer

import faiss
import matplotlib.pyplot as plt
import numpy as np

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
    t1 = time()
    print("Embedding started")
    embeddings = model.encode(sentences)
    print(f"Embeddings shape: {embeddings.shape}")
    print("Embedding finished")
    t2 = time()
    return embeddings, t2-t1


def create_faiss_index(embeddings):
    t1 = time()
    print("FAISS index construction started")
    DIMENSIONS = embeddings.shape[1]
    index = faiss.IndexFlatL2(DIMENSIONS)
    index.add(embeddings)
    print(f"Index: {index.ntotal}")
    print("FAISS index construction finished")
    t2 = time()
    return index, t2-t1


model = initialize_model(MODEL_NAME)
dataset = load_dataset_by_id(DATASET_ID)

ns = []
ts_embeddings = []
ts_index = []

for n in np.linspace(1000, 10000, 20):
    ns.append(n)
    sentences = build_sentences(dataset, 0, int(n))
    embeddings, t_embeddings = create_embeddings(model, sentences)
    index, t_index = create_faiss_index(embeddings)
    ts_embeddings.append(t_embeddings)
    ts_index.append(t_index)

fig = plt.figure(figsize=(10, 10))

plt.subplot(2, 1, 1)
plt.plot(ns, ts_embeddings, "b-")
plt.title("Embeddings creation")

plt.subplot(2, 1, 2)
plt.plot(ns, ts_index, "m-", label="index creation")
plt.title("Index creation")

# povolení zobrazení mřížky
plt.grid(True)

fig.savefig("embeddings.png")

# zobrazení grafu
fig.show()

