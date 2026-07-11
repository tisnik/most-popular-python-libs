# Framework LangChain
#
# - inicializace rozhraní k modelu poskytovaného přes OpenAI
# - poslání dotazu do jazykového modelu
# - tisk odpovědi v naformátované podobě

from pprint import pprint
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-4o-mini")
response = llm.invoke("Say Hi")
pprint(response)
