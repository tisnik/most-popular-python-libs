# Framework LangChain
#
# - inicializace rozhraní k modelu poskytovaného přes OpenAI
# - poslání dotazu do jazykového modelu
# - tisk celé struktury odpovědi (nikoli pouze textu)

from langchain_openai import ChatOpenAI
from langchain_core.messages.human import HumanMessage

import pprint

llm = ChatOpenAI(model_name="gpt-4o-mini")
response = llm.generate([[HumanMessage("Say Hi")]])
pprint.pprint(response.llm_output)
