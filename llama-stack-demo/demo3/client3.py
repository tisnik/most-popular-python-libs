from llama_stack.distribution.library_client import LlamaStackAsLibraryClient
from llama_stack_client import LlamaStackClient

client = LlamaStackAsLibraryClient("run.yaml")
client.initialize()

print(f"Using Llama Stack version {client._version}")

models = client.models.list()

for model in models:
    print(model)
