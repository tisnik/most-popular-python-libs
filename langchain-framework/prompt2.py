# Framework LangChain
#
# - jednoduchý řetězec
# - nastavení parametrů jazykového modelu
# - poslání dotazu do jazykového modelu
# - tisk odpovědi

from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

prompt = PromptTemplate(
    input_variables=["language"],
    template="How to say 'hi' in {language} language?",
)


llm = ChatOpenAI(model_name="gpt-4o-mini")
chain = LLMChain(prompt=prompt, llm=llm)

response = chain.invoke("Czech")
print(response)
