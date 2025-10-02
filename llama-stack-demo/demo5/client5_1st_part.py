from pathlib import Path
import uuid
from llama_stack_client import LlamaStackClient

client = LlamaStackClient(base_url="http://localhost:8321")
print(f"Using Llama Stack version {client._version}")

vector_store_name= f"vec_{str(uuid.uuid4())[0:8]}"
print(f"Vector store name: {vector_store_name}")

vector_store = client.vector_stores.create(name=vector_store_name)
vector_store_id = vector_store.id

print(f"Vector store ID: {vector_store_id}")

path=Path("README.TXT")
print(f"File path: {path}")

file_create_response = client.files.create(file=path, purpose="assistants")
print(f"File create response: {file_create_response}")

file_ingest_response = client.vector_stores.files.create(
    vector_store_id=vector_store_id,
    file_id=file_create_response.id,
)
print(f"File ingest response: {file_ingest_response}")

