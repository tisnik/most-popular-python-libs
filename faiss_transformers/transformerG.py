from sentence_transformers import SentenceTransformer
import faiss
from datasets import load_dataset

MODEL_NAME = "paraphrase-MiniLM-L6-v2"
DATASET_ID = "polygraf-ai/human-sentences-1M-sample-v2"


def initialize_model(model_name, dtype):
    print("Model initialization started")
    model = SentenceTransformer(model_name, model_kwargs={"torch_dtype": dtype})
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


for dtype in ["float32", "float16", "bfloat16"]:
    model = initialize_model(MODEL_NAME, dtype)
    dataset = load_dataset_by_id(DATASET_ID)

    sentences = build_sentences(dataset, 0, 10)
    embeddings = create_embeddings(model, sentences)
    index = create_faiss_index(embeddings)

    embeddings.dump(f"embeddings.{dtype}")
    faiss.write_index(index, f"index.{dtype}")

