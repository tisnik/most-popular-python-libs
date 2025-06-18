from llama_stack_client import LlamaStackClient

PROMPT = "Say Hello"

client = LlamaStackClient(base_url="http://localhost:8321")

response = client.inference.chat_completion(
    messages=[{"role": "user", "content": PROMPT}],
    model_id=client.models.list()[0].identifier,
)

print(response.completion_message.content)
