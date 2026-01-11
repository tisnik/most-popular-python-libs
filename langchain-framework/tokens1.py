# Framework LangChain
#
# - zjištění počtu tokenů pro zadaný řetězec

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-4o-mini")
print(llm.get_num_tokens("What is firefox?"))
