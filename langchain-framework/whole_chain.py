from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain


DOCUMENT_PATH = "README.TXT"

loader = TextLoader(DOCUMENT_PATH)
text_document=loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
documents = text_splitter.split_documents(text_document)


embeddings = OpenAIEmbeddings()

vectorstore = FAISS.from_documents(documents, embeddings)

query = "What is Zonk?"
result = vectorstore.similarity_search(query)

print("Similarity search:")
print(result[0].page_content)
print()


prompt = ChatPromptTemplate.from_template(
    """
    You are an expert assistant. Answer the following question based only on the provided context:

    <context>
    {context}
    </context>

    Question: {input}
    """
)


llm = ChatOpenAI(model_name="gpt-4o-mini")
retriever = vectorstore.as_retriever()

document_chain = prompt | llm
chain = create_retrieval_chain(retriever, document_chain)

response = chain.invoke({
    "input": "What is Zonk?",
})

print("And the answer is:")
print(response["answer"])
