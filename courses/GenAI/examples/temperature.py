from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)
response = llm.invoke("Say Hi")
print(response)
