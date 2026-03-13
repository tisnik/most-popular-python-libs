from sentence_transformers import SentenceTransformer

def embeddings_info(embeddings):
    print(f"Embeddings shape: {embeddings.shape}")
    print(f"Embeddings type:  {type(embeddings)}")
    print(f"Embeddings dtype: {embeddings.dtype}")
    print(f"Size in bytes:    {embeddings.nbytes}")
    print()


model = SentenceTransformer("mixedbread-ai/mxbai-embed-large-v1")
print(model)

sentence = "The rain in Spain falls mainly on the plain"

ubinary_embeddings = model.encode(sentence, precision="ubinary")
embeddings_info(ubinary_embeddings)

for i, byte in enumerate(ubinary_embeddings):
    print(format(byte, "08b"), end="")
    if i % 8 == 7:
        print()
