# Framework LangChain
#
# - tisk všech dostupných modelů získaných od poskytovatele

from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
models = client.models.list()

for model in models:
    print(model.id)
