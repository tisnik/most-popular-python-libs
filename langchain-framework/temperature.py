# Framework LangChain
#
# - inicializace rozhraní k modelu poskytovaného přes OpenAI
# - nastavení parametrů jazykového modelu
# - poslání dotazu do jazykového modelu
# - tisk odpovědi

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)
response = llm.invoke("Say Hi")
print(response)
