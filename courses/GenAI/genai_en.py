# # GenAI and Python
# 
# ![Python](images/python.png)
# 
# Pavel Tišnovský,
# tisnik@centrum.cz
# 
# ---
# 
# ## Table of content
#
# * Theory
#     - Machine learning and artifical intelligence
#     - Models, training, evaluation
#     - Neural networks
#     - Generative artifical intelligence
#     - Frameworks for GenAI
#     - Elementary features of LLMs
#     - OpenAI and other standardized APIs
#     - Llama Stack framework
#     - Langchain framework
#     - RAG (Retrieval-augmented generation)
#     - Evuation
# * Practice
#     - LLM call
#     - Langchain
#     - Text tokenization
#     - Embedding models usage
#     - Vector similarity search
#     - FAISS
#     - SentenceTransformer
#     - PgVector
#     - Final project
#
# ---
#
# # Theory
#
# ---
#
# ### Artifical intelligence
#
# 
# * Definition
#     - construction of machines that can perform activities requiring intelligence if performed by humans (Marvin Minsky, 1967)
#     - there are, however, alternative definitions
# * Modeling the human mind
#     - top-down (psychology)
#     - bottom-up (neuroscience)
#     - middle-out (computer science)
# * Intelligent behavior can emerge from the combination of a large number of simple systems
#     - concept of neural networks
# 
# ---
#
# ## Development of artificial intelligence
# 
# * 1943–1955
#      - first ideas that something like this could realistically arise
#      - Boolean model of the neuron
#      - A. Turing
#          - Computing Machinery and Intelligence
# * 1956
#      - McCarthy (LISP)
#      - (probably) used the term AI for the first time
#      - Newell and Simon: Logic Theorist
# *high expectations of progress in the following years
#      - partial solutions to various problems succeeded
#      - practically a new discovery every month
# * around 1965
#      - sobering up
#      - although many problems had been solved, they were trivial
#      - limits were found that could not be overcome
#      - first "AI winter"
# * 1970s
#      - knowledge-based systems
#      - development in many areas (oil exploration, etc.)
# * early 1980s
#      - large investments in AI
#      - expectations were not met
#      - then the second "AI winter" occurs
# * second half of the 1980s
#      - development of neural networks (which was not new)
# * 1995
#      - SOAR systems (State, Operator and Result)
# * 2000
#      - big data (which continues today)
#      - but so far no large volumes
#      - "wow" effect at the level of AI
# * 2010
#      - deep learning
# * 2020
#      - LLMs (prompt engineering, not fine-tuning)
# * present
#      - LLMs
#      - generative AI
# 
# ---
# 





#
# ---
#
# ### PGVector and Sentence transformers
#
# * zápis vektorizovaných vět do tabulky

import psycopg2
from sentence_transformers import SentenceTransformer

from pgvector.psycopg2 import register_vector

model = SentenceTransformer("paraphrase-MiniLM-L6-v2")

print(model)

sentences = [
    "The rain in Spain falls mainly on the plain",
    "The tesselated polygon is a special type of polygon",
    "The quick brown fox jumps over the lazy dog",
    "To be or not to be, that is the question",
    "It is a truth universally acknowledged...",
    "How old are you?",
    "The goat ran down the hill"
]

embeddings = model.encode(sentences)
print(f"Embeddings shape: {embeddings.shape}")

connection = psycopg2.connect(
    host="", port=5432, user="tester", password="123qwe", dbname="test"
)

register_vector(connection)

for vector in embeddings:
    print(type(vector), vector.shape)
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO v384 (embedding) VALUES (%s)", (vector, ))

connection.commit()

#
# ---
#
# ### Searching based on semantic text similarity

import psycopg2
from sentence_transformers import SentenceTransformer

from pgvector.psycopg2 import register_vector

connection = psycopg2.connect(
    host="", port=5432, user="tester", password="123qwe", dbname="test"
)

print(connection)
register_vector(connection)


model = SentenceTransformer("paraphrase-MiniLM-L6-v2")
print(model)


def find_similar_sentences(connection, query_sentence, k):
    print(f"Query: {query_sentence}")
    print(f"Most {k} similar sentences:")

    vector = model.encode(query_sentence)

    with connection.cursor() as cursor:
        query = """
            SELECT id, embedding
              FROM v384
             ORDER BY embedding <-> %s::vector
             LIMIT %s
        """
        cursor.execute(query, (vector, k))
        records = cursor.fetchall()
        for record in records:
            print(record[0])
    print("-"*40)


find_similar_sentences(connection, "The quick brown fox jumps over the lazy dog", 3)
find_similar_sentences(connection, "quick brown fox jumps over lazy dog", 3)
find_similar_sentences(connection, "The quick brown fox jumps over the angry dog", 3)
find_similar_sentences(connection, "The quick brown cat jumps over the lazy dog", 3)
find_similar_sentences(connection, "What is your age?", 3)
find_similar_sentences(connection, "Shakespeare", 3)
find_similar_sentences(connection, "animal", 3)
find_similar_sentences(connection, "geometry", 3)
find_similar_sentences(connection, "weather", 3)

#
# ---
#
# # Final project realization
#
# - now we know all the parts of final language chain
# - how to call LLM
# - how to vectorize text
# - how to perform document chunking
# - how to perform vector similarity search
# - time to implement everything on one place!
#

# ---
#
# ### Project configuration
#
# ```toml
# [project]
# name = "docs"
# version = "0.1.0"
# description = "Add your description here"
# readme = "README.md"
# requires-python = ">=3.13"
# dependencies = [
#     "bs4>=0.0.2",
#     "datasets>=4.8.4",
#     "faiss-cpu>=1.13.2",
#     "langchain>=1.2.13",
#     "langchain-classic>=1.0.3",
#     "langchain-community>=0.4.1",
#     "langchain-openai>=1.1.12",
#     "matplotlib>=3.10.8",
#     "sentence-transformers>=5.3.0",
# ]
# ```

# ---
#
# ### Chain implementation, including RAG
#
# - from question to answer, including RAG
# - sequence of several steps
#     1. text document loading
#     2. chunking
#     3. embedded model construction
#     4. an example, how similarity search works (which text will be send to LLM)
#     5. language chain preparation
#     6. LLM call, including RAG part
#     7. display response
#
# Remark: we will use FAISS, but it would be possible to use PgVector as well

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain

# text document loading

DOCUMENT_PATH = "README.TXT"

loader = TextLoader(DOCUMENT_PATH)
text_document=loader.load()

# chunking

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
documents = text_splitter.split_documents(text_document)

# embedded model construction

embeddings = OpenAIEmbeddings()

vectorstore = FAISS.from_documents(documents, embeddings)

# an example, how similarity search works (which text will be send to LLM)

query = "What is Zonk?"
result = vectorstore.similarity_search(query)

print("Similarity search:")
print(result[0].page_content)
print()

# language chain preparation

prompt = ChatPromptTemplate.from_template(
     "You are an expert assistant. Answer the following question based only on the provided context:" + \
     "<context>" + \
     "{context}" + \
     "</context>" + \
     "Question: {input}"
)

llm = ChatOpenAI(model_name="gpt-4o-mini")
retriever = vectorstore.as_retriever()

document_chain = prompt | llm
chain = create_retrieval_chain(retriever, document_chain)

# LLM call, including RAG part

response = chain.invoke({
    "input": "What is Zonk?",
})

# display response

print("And the answer is:")
print(response["answer"])

#
#
# ---
#
# ## Other areas where the project can be expanded
#
# * MCP (Model Context Protocol)
# * Agents
# * Guardrails
# * Different technologies for RAG
#    - hybrid search
#    - Milvus atd.
# * ...we don't know what will be found next months, years
#

#
# ---
#
# ## Appendix: MCP client

from time import time

from mcp import ClientSession
from mcp.client.sse import sse_client


async def run(i):
    """MCP client implementation."""
    async with sse_client(url="http://localhost:8000/sse") as (read, write):
        async with ClientSession(read, write) as session:
            t1 = time()
            print(f"Client #{i} initialization")
            print()

            await session.initialize()

            # resource reading: without selector
            data = await session.read_resource("greeting://")
            print("Data returned:", data)
            print("Type:", type(data))
            text = data.contents[0].text
            print("Text:", text)
            print()

            # resource reading: with selector
            data = await session.read_resource("greeting://Pavel")
            print("Data returned:", data)
            print("Type:", type(data))

            text = data.contents[0].text
            print("Text:", text)
            print()

            # tool call
            data = await session.call_tool("factorial", arguments={"n": 10})
            factorial = data.content[0].text
            print("10!=", factorial)
            print()

            t2 = time()
            difftime = t2 - t1
            print(f"Client has finished in {difftime} seconds")
            print()


async def main():
    clients = [run(i) for i in range(10)]
    await asyncio.gather(*clients)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())

#
# ---
#
# ## MCP server

from time import sleep

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Test")

SLEEP_AMOUNT=0.5


@mcp.tool()
def factorial(n: int) -> int:
    """Factorial computation."""
    print("Factorial computation started")
    f = 1
    for x in range(1, n + 1):
        f *= x
    sleep(SLEEP_AMOUNT)
    print("Factorial computation finished")
    return f


@mcp.resource("greeting://")
def greeting1() -> str:
    """Reply containing greeting."""
    print("Resource preparation started")
    sleep(SLEEP_AMOUNT)
    print("Resource preparation finished")
    return "Hello, dear client!"


@mcp.resource("greeting://{name}")
def greeting2(name: str) -> str:
    """Reply containing greeting to given person."""
    print("Resource preparation started")
    sleep(SLEEP_AMOUNT)
    print("Resource preparation finished")
    return f"Hello, {name}!"


if __name__ == "__main__":
    mcp.run(transport="sse")

#
# ---
#
# # Thank you!
#

