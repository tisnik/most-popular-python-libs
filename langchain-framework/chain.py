# Framework LangChain
#
# - jednoduchý řetězec vytvořený operátorem |
# - nastavení parametrů jazykového modelu
# - poslání dotazu do jazykového modelu
# - tisk odpovědi

from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate.from_template("How to say 'hi' in {language} language?")

llm = ChatOpenAI(model_name="gpt-4o-mini")

chain = prompt | llm | StrOutputParser()

response = chain.invoke({"language": "Czech"})
print(response)
