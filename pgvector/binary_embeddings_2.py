from sentence_transformers import SentenceTransformer

def embeddings_info(embeddings):
    print(f"Embeddings shape: {embeddings.shape}")
    print(f"Embeddings type:  {type(embeddings)}")
    print(f"Embeddings dtype: {embeddings.dtype}")
    print(f"Size in bytes:    {embeddings.nbytes}")
    print()
    print(embeddings)


model = SentenceTransformer("mixedbread-ai/mxbai-embed-large-v1")
print(model)

sentence = "The rain in Spain falls mainly on the plain"

embeddings = model.encode(sentence)
embeddings_info(embeddings)
