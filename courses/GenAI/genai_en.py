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
# ## Introduction
#
# * Artifical intelligence
# * Evolution of artifical intelligence
# * Machine learning
# * The relationship between machine learning and artificial intelligence
#
# ---
#
# ### Artifical intelligence
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
# ## Machine learning
# 
# * subset of artifical intelligence
# * changing system internal state during training
# * several variants how to implement machine learning
# * "statistical learning"
# * usually it is not fully automated
#     - needs smart (strategic) decisions
#     - model selection
#     - model hyperparameters tuning
#     - input data split
#     - data filtration
# * system tries to find patterns and links in data
# 
# ---
# 
# ## The relationship between machine learning and artificial intelligence
# 
# ![vztah.png](images/ai_ml_dl.png)
# 
# * Artifical intelligence (AI)
#     - machine learning (ML)
#     - deep learning (DL)
#     - robotics
#     - neural networks (NN)
#     - native language processing (NLP)
# * AI > ML > NN > DL
# 
# * Artifical intelligence
#     - discovery
#     - derivation
#     - justification
# * Machine learning
#     - (sophisticated) analysis
#     - prediction (!)
#     - decision making (classification or regression)
# 
# ---
# 
# ### Why machine learning?
#
# * We require the machine to learn how to solve given problem
#     - solution is too complicated
#     - problem is evolving/changing over time
#     - human labor is expensive
#     - too much data to be processed by humans
#
# ---
#
# ### Typical applications of machine learning
#
# * Pattern recognition
#     - objects, persons, face recognition
#     - spoken words
#     - spam
#     - diagnosis in medicine
# * Anomaly recognition
#     - atypical financial transactions
#     - atypical data from sensors (nuclear plant)
# * Forecasting
#     - stock exchange prices
#     - which movies/videos will be watched by given person
#     - age of person on photo
# * Clustering
#     - messages with similar content
#     - group of customers with similar behaviour/preference
#
# ---
#
# ## Basic concepts
#
# * Data set
#      - training data
#      - test or evaluation data
# 
# ![dataset.png](images/dataset.png)
# 
# ---
# 
# ### Techniques used in machine learning
#
# * Supervised learning
#    - also called "predictive modeling"
#    - we know "categories" (answers)
# * Unsupervised learning
#    - we don't know answers
#    - model must find structures/patterns in data
#    - typically based on clustering algorithms
# 
# ![ml.png](images/ml.png)
# 
# ---
# 
# ### Supervised learning
#
# 1. Training based on input data
#     - model have to learn relationships between inputs and outputs
# 2. Predictions based on different(!) data set
#     - data must be split!
# 3. Results
#     - classification: will he buy A, B, or C?
#     - regression: numeric value or values
#
# ---
#
# ### Unsupervised learning
#
# 1. Training based on input data
#    - but the model does not know answers
# 2. Clustering
# 3. Latent and factor analysis is possible too
#
# ---
#
# ### Other variants
#
# 1. Combination of both methods presented above
# 2. Learning with feedback
#     - passive
#     - active
#
# ---
#
# ### Machine learning models
# 
# * ANN
# * Desicion trees
# * Support-vector machine
# * Regression analysis
# * Bayession networks
# * Genetics algorithms
# * Neural networks
# 
# ---
#
# ### Where to start?
#
# 1. Which attributes to use from the data?
# 2. Which model to choose?
# 3. How to optimize for better performance?
# 4. How to create a model that will be suitable for data unknown to it?
# 5. How to estimate a model's suitability for unknown data?
# 
# ---
#
# ### Data reduction
# * the relationship between ML and data compression
# * prediction
# * so‑called optimal compression
#     - for prediction, arithmetic coding can be used
#
# ---
# 
# ### Data reduction
# 
# ![reduction.png](images/reduction.png)
# 
# ---
# 
# ### Data reduction (supervised)
# 
# ![reduction_supervised.png](images/reduction_supervised.png)
# 
# ---
#
# ### Underfitting and Overfitting
# 
# * Underfitting
#     - small training dataset
#     - model too simple
#     - data represent only a small sample of the full value range
# * Overfitting
#     - strong dependence on training data
#     - reduced ability to work with unseen data
#     - using a higher-degree polynomial when a linear one would suffice
# 
# ---
# 
# ### Overfiting
# 
# ![overtrain.png](images/overtraining.png)
# 
# ---
#
# ### Model performance
#
# * For completely new (unseen) data!
#     - not for the training set
#     - common mistake
#
# ---
#
# ### Cross-validation
#
# * split the data into folds
#     - for example into 1/10
#     - 9/10 for training
#     - 1/10 for testing
# 
# ---
#
# ## Neural networks
#
# * Connection of so-called neurons
#     - Neuron model
#     - Neuron connections
#     - Inputs and outputs
#
# ---
#
# ### Neuron model
# 
# ![neuron.png](images/neuron.png)
# 
# * any number of inputs
# * typically only one output
# * weighted inputs
# * activation function
# 
# y = f(w1x1 + w2x2 + … + wnxn)
# 
# ---
# 
# ### Bias
# 
# ![bias.png](images/bias.png)
# 
# y = f(w0 + w1x1 + w2x2 + … + wnxn)
# 
# ---
# 
# ### Activation function
# 
# * The only non-linearity in the whole model
# * Many activation functions can be used
# 
# ---
# 
# ### Activation function
# 
# ![akt1.png](images/akt_1.png)
# 
# ---
# 
# ### Activation function
# 
# ![akt2.png](images/akt_2.png)
# 
# ---
# 
# ### Feed-forward network
# 
# * Input layer
# * Hidden layers
# * Output layer
# 
# ---
# 
# ### Feed-forward síť
# 
# ![ff.png](images/ff.png)
# 
# ---
# 
# ### Too many layers
# 
# * Model stops training or trains very slowly
#     - vanishing gradient problem
#     - "Less is sometimes more"
# 
# ---
# 
# ### Convolutional neural networks
# 
# * Used to analyse raster images
#     - offsets, skews, rotations etc.
#     - possible to solve using classic NN
#     - but it is too complicated (RAM, CPU, time)
#     - the same weights stored for many neurons on the same place
#     - convolutional and subsampling layers
# 
# ---
# 
# ### Convolutional neural networks
# 
# * Typical configuration
#     - input layer
#     - convolutional layer
#     - subsampling layer
#
# ---
#
# # Generative AI
#
# ![LS](images/lsc.jpg)
#
# ---
#
# ## Frameworks for GenAI
# * langchain
# * langgraph
# * autogen
# * metaGPT
# * phidata
# * CrewAI
# * pydanticAI
# * controlflow
# * langflow
# * LiteLLM (???)
# * Llama Stack
# 
# ---
# 
# ## Do we really need sophisticated frameworks?
#
# * some operations can be done without framework, just by using library
# * for example OpenAI library
# * also possible to use LiteLLM

# 
# ---
# 
# ### List of all models available
# - it is based on OpenAI package
# - key is read from environment variable

from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
models = client.models.list()

for model in models:
    print(model.id)

# ---
# 
# ## Do we really need sophisticated frameworks?
#
# * Quota handling
# * Conversation memory
# * Context memory
# * Guardrails
# * RAG
# * BYOK
# * MCP
# * Agents
# * A2A
# 
# ---
# 
# ## Llama Stack
# 
# ![Llama Stack logo](images/llama_stack_logo.png)
# 
# ---
#
# ## What is Llama Stack?
#
# * Framework for making AI-based applications
#     - chat bots
#     - generative AI (GenAI)
#     - training and evaluation
# * Real framework independent on programming language
#     - system of providers
#     - RAG, quota handling, guardrails, metrics etc.
# 
# ---
# 
# ### Simplest Llama Stack usage
# 
# * LLM call
# * LLM response handling
# * "chatbot v.0.0.1"
# 
# ---
# 
# ### Real requirements, it's larger list
# 
# * RAG
# * Conversation history
# * Conversation forking
# * Facts about user
# * MCP calls
# * Quotas
# * Query validation, response redaction
# * Multiple LLMs calls, response evaluation
# 
# ---
# 
# ### API and providers
# 
# * Fully configurable
# * It is possible to get a list of available APIs
# * It is possible to get a list of available providers
# * Warning: providers have its own dependencies
# 
# ---
# 
# ![Providers](images/llama_stack_providers.png)
# 
# ### Providers
#
# * Agents
#     - interaction with agents
# * Inference
#     - interface to LLM models and embedding models
# * VectorIO
#     - historically interface to vector databases
#     - now it supports full text search too
# * Safety
#     - query validation, response redaction
# * Telemetry
#     - telemetry
#     - OpenTelemetry etc.
# * Eval
#     - evaluation of LLM responses
# * DatasetIO
#     - reads and writes to data sets on file system
#     - it can be a local file system if needed
#
# ---
# 
# ### Communication with Llama Stack
# 
# * CLI
# * REST API
# * As a regular library (Python etc.)
# * Llama Stack client
#     - supports REST API
#     - supports LS as a library (async code)
#
# ---
# 
# ### Llama Stack client
# 
# * Python
# * Swift
# * Kotlin
# * Node.js
#
# ---
# 
# ### Llama Stack as a library
# 
# ![LS1](images/llama_stack_as_library.png)
# 
# ---
# 
# ### Llama Stack as separate service
# 
# ![LS1](images/llama_stack_as_service.png)
# 
# ---
# 
# ### Llama Stack in a container
# 
# ![LS1](images/llama_stack_in_container.png)
# 
# ---
#
# ### An example of service based on Llama Stack
#
# * REST API based on top of Llama Stack API
# * Supports LS in library and service mode
# * Implemented as asynchronous code (Python)
# 
# ---
# 
# ![LS1](images/llama_stack_arch.png)
# 
# ---
#
# ![Langchain logo](images/langchain.png)
# 
# ---
# 
# ### Langchain
# 
# * Framework for GenAI and Python
# * Chatbots
# * RAG
# * Conversation memory
# * Conversation summarization
# * Synthetic data generation
# 
# ---
# 
# ### Langchain
# 
# * Simple tasks can be implement by simple code
# * In some cases just few lines of cide
# * Pipe operator | to create pipeline
# * Supports RAG
# 
#
# ---
#
# ## Evaluation
#
# ### Why evaluation?
#
# * Measure performance
# * Ensure good user experience
# * Detect bias & harm
# * Comply with ethical & legal standards
#
# ### Benefits of Evaluation
#
# * Improvement:
#     - Pinpoints weaknesses (e.g., hallucinations)
#     - Enables data-driven model tuning
# * Benchmarking:
#     - Compare models (GPT, Gemini, Granite, etc.)
#     - Ensures reliability over time
#
# ### Lightspeed evaluation framework
#
# * Multi-Framework LLM as a Judge
#      - Ragas, DeepEval and custom implementations
# * Turn & Conversation-Level
#       - Individual queries and multi-turn conversations
# * Tools/Agents Support
# * LLM Providers
#       - OpenAI, Watsonx, Gemini, vLLM and others
# * Setup/Cleanup Scripts
# * Statistical Analysis
#
# ---
# 
# # Practical part
#
# ![Work](images/work.jpg)
#
# - LLM call
# - Langchain
# - Text tokenization
# - Embedding
# - Vector similarity search
# - PgVector
# - FAISS
# - Evalation
#
# ---
# 
# ### Llama Stack client
# 
# * Client library for Python
# 
# ```bash
# uv init
# uv add llama-stack-client
# ```
# 
# ---
#

# 
# ### Llama Stack as separate service
# 

# List of all available models

from llama_stack_client import LlamaStackClient

client = LlamaStackClient(base_url="http://localhost:8321")

print(f"Using Llama Stack version {client._version}")

models = client.models.list()

for model in models:
    print(model)

# ---
# 
# ### Llama Stack as a library
# 

# List of all available models

from llama_stack.distribution.library_client import LlamaStackAsLibraryClient

client = LlamaStackAsLibraryClient("run.yaml")
client.initialize()

print(f"Using Llama Stack version {client._version}")

models = client.models.list()

for model in models:
    print(model)

# ---
#
# ### Communication with LLM

from llama_stack_client import LlamaStackClient

client = LlamaStackClient(base_url="http://localhost:8321")

print(f"Using Llama Stack version {client._version}")

models = client.models.list()
model_id = models[0].identifier

print(f"Using model {model_id}")

response = client.chat.completions.create(
    model=model_id,
    messages=[{"role": "user", "content": "What is the capital of France?"}]
)

print(response.to_json())

# ---
#
# ### Llama Stack evolution
#
# * API changes
# * Some API might be dropped
#     - deprecation
# * Agent API replaced by OpenAI API
# * Might be stabilized in version 0.7.0 ???
#
# ---

# ### Newer API usage

from llama_stack_client import LlamaStackClient

client = LlamaStackClient(base_url="http://localhost:8321")

print(f"Using Llama Stack version {client._version}")

models = client.models.list()
model_id = models[0].identifier

print(f"Using model {model_id}")

response = client.chat.completions.create(
    model=model_id,
    messages=[{"role": "user", "content": "What is the capital of France?"}]
)

print(response.to_json())

# ---
# 
# ### Retrieving information from documents
# 
# * RAG
# * And other inputs
#     - semantic search
#     - fulltext search
#     - hybrid search
# 
# ---
# 

# ### Processing documents

# * connection to Llama Stack
# * vector store construction
# * vector store initialization

import uuid
from pathlib import Path
from llama_stack_client import LlamaStackClient

client = LlamaStackClient(base_url="http://localhost:8321")
print(f"Using Llama Stack version {client._version}")

vector_store_name= f"vec_{str(uuid.uuid4())[0:8]}"
print(f"Vector store name: {vector_store_name}")

vector_store = client.vector_stores.create(name=vector_store_name)
vector_store_id = vector_store.id

print(f"Vector store ID: {vector_store_id}")

# * add a new document into vector store
path=Path("cesta_k_souboru.md")
print(f"File path: {path}")

file_create_response = client.files.create(file=path, purpose="assistants")
print(f"File create response: {file_create_response}")

file_ingest_response = client.vector_stores.files.create(
    vector_store_id=vector_store_id,
    file_id=file_create_response.id,
)
print(f"File ingest response: {file_ingest_response}")

# * now the document has been processed
# * retrieve output/answer from the document

models = client.models.list()
model_id = models[0].identifier

print(f"Using model {model_id}")

MODEL_ID="openai/gpt-4-turbo"

# helper function

def print_rag_response(response):
    print(f"ID: {response.id}")
    print(f"Status: {response.status}")
    print(f"Model: {response.model}")
    print(f"Created at: {response.created_at}")
    print(f"Output items: {len(response.output)}")

    for i, output_item in enumerate(response.output):
        if len(response.output) > 1:
            print(f"\n--- Output Item {i+1} ---")
        print(f"Output type: {output_item.type}")

        if output_item.type in ("text", "message"):
            print(f"Response content: {output_item.content[0].text}")
        elif output_item.type == "file_search_call":
            print(f"  Tool Call ID: {output_item.id}")
            print(f"  Tool Status: {output_item.status}")
            print(f"  Queries: {', '.join(output_item.queries)}")
            print(f"  Results: {output_item.results if output_item.results else 'None'}")
        else:
            print(f"Response content: {output_item.content}")

# retrieve response from vector database

response = client.responses.create(
    model=MODEL_ID,
    input="some question",
    tools=[
        {
            "type": "file_search",
            "vector_store_ids": [vector_store_id],
        }
    ]
)

print_rag_response(response)

# ---
# 
# ### Example 1/2
# 
# * Document:
#     - `README.TXT` from the Supaplex game
# * Relevant part from this document:
# 
# ```plaintext
# [a round rock] - ZONK
#        This is another very common obstacle (and usually a very
#        unpleasant one) a Zonk tends to fall down whenever possible
#        (i.e. there is a void underneath). Be careful, when a Zonk
#        falls on you (Murphy) you will explode (read: die). Murphy can
#        push Zonks to the side (not up and down) if nothing is blocking
#        the Zonk (i.e. there is a void on the other side). Murphy can
#        only push one Zonk at a time, so watch out when dropping Zonks
#        next to each other! With some good timing, you can also drop
#        Zonks on Electrons (see below) or Snik-snaks (see below) which
#        will explode (and not bother you again). Zonks have the nasty
#        habit of falling SIDEWAYS off Ram-Chips (see below) and other
#        Zonks if possible (i.e. there is a void to the side), on all
#        other objects the Zonks will lie steady.
# ```
# 
# ---
# 
# ### Example 2/2
# * Query:
# ```plaintext
# What is Zonk?
# ```
# * Response:
# ```plaintext
# "ZONK" refers to an element in the videogame Supaplex. In the
# game, a Zonk is depicted as a round rock, and it is a common and typically
# unpleasant obstacle. Zonks tend to fall downwards whenever possible, for
# instance, if there is a void directly underneath them. Players must be cautious
# as a Zonk falling on the character (Murphy) results in an explosion and
# game-over for the player. Murphy can push Zonks laterally (but not vertically)
# if there is space for them to move, but can only push one Zonk at a time. Good
# timing is needed to use Zonks strategically, such as dropping them on top of
# enemies (like Snik-snaks) to eliminate them through explosions.
# ```
# 
# ---
#
# ### Current situation about Llama Stack
#
# * Meta -> vLLM
# * Compatibility with responses API (OpenAI)
# * Agentic flow support (preliminary)
# * Some functions are being removed(!)
# * The platform as a whole is unstable
# * Usage of Llama Stack is at risk!
#
# ---
#
# ![Langchain logo](images/langchain.png)
#
# * we'll start with very simple examples
# * later examples
#    - LLM calls
#    - RAG
#
# ---

# ### Retrieving response from LLM
# - OpenAI interface initialization
# - question is sent to LLM
# - response is printed

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-4o-mini")
response = llm.invoke("Say Hi")
print(response)


#
# ---
#

# ### Object of type `response`
# - OpenAI interface initialization
# - question is sent to LLM
# - response is printed (formatted)

from pprint import pprint
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-4o-mini")
response = llm.invoke("Say Hi")
pprint(response)

#
# ---
#

# ### Temperature settings
# - OpenAI interface initialization
# - Model parameters are fine tuned (temperature in this case)
# - question is sent to LLM
# - response is printed (formatted)

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)
response = llm.invoke("Say Hi")
print(response)

#
# ---
#

# ### Templates
# - prompt as a template
# - parameters is put into the template
# - question is sent to LLM
# - response is printed

from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

prompt = PromptTemplate.from_template("How to say 'hi' in {language} language?")

llm = ChatOpenAI(model_name="gpt-4o-mini")
chain = LLMChain(prompt=prompt, llm=llm)

response = chain.invoke("Czech")
print(response)

#
# ---
#

# ### Colon (pipe)
# - prompt as a template
# - parameters is put into the template
# - question is sent to LLM
# - response is printed

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

#
# ---
#

# ### Řetězce (kolony)
# - prompt as a template
# - parameters is put into the template
# - question is sent to LLM
# - response is printed

from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate.from_template("How to say 'hi' in {language} language?")

llm = ChatOpenAI(model_name="gpt-4o-mini")

chain = prompt | llm | StrOutputParser()

response = chain.invoke({"language": "Czech"})
print(response)


#
# ---
#

# ### Conversation memory
# - memory with conversation
# - facts are sent to the LLM
# - response depends on facts

from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

llm = ChatOpenAI(model_name="gpt-4o-mini")

memory = ConversationBufferMemory()
chatbot = ConversationChain(llm=llm, memory=memory)

print(chatbot.invoke("Hi, I'm Pavel and I live in Czechia."))
print(chatbot.invoke("What's my name?"))
print(chatbot.invoke("Where I live?"))

#
# ---
#

# ### Token handling
# - figuring out number of tokens to represent a string

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-4o-mini")
print(llm.get_num_tokens("What is firefox?"))

#
# ---
#

# ### Token handling
#
# - OpenAI LLM connection initialization
# - send request to LLM
# - print the whole returned structure

from langchain_openai import ChatOpenAI
from langchain_core.messages.human import HumanMessage

import pprint

llm = ChatOpenAI(model_name="gpt-4o-mini")
response = llm.generate([[HumanMessage("Say Hi")]])
pprint.pprint(response.llm_output)

#
# ---
#

# ### Documents handling - text documents loader
#
# - object initialization for loading text document
# - one text document loading and processing
# - print the returned document structure

from langchain_community.document_loaders import TextLoader

DOCUMENT_PATH = "documents/EPL-2.0.txt"

loader = TextLoader(DOCUMENT_PATH)
print(loader)

text_documents= loader.load()

print(f"Number of documents: {len(text_documents)}")

for text_document in text_documents:
    print()
    print("-"*80)
    print()
    print(text_document)


#
# ---
#
# ### Document loading - printing metadata about processed document
#
# - object initialization for loading text document
# - one text document loading and processing
# - print document type + document metadata
# - print the returned document structure

from langchain_community.document_loaders import TextLoader

DOCUMENT_PATH = "documents/EPL-2.0.txt"

loader = TextLoader(DOCUMENT_PATH)
print(loader)

text_documents= loader.load()

print(f"Number of documents: {len(text_documents)}")

for text_document in text_documents:
    print()
    print("-"*80)
    print()
    print("Type:", text_document.type)
    print("Metadata:", text_document.metadata)
    print()
    print(text_document.page_content)

#
# ---
#
# ### Document loading - printing metadata about processed document
#
# - object initialization for loading text document
# - one PDF document loading and processing
# - print document type + document metadata
# - print the returned document structure

from langchain_community.document_loaders import TextLoader

DOCUMENT_PATH = "documents/assemblery.txt"

loader = TextLoader(DOCUMENT_PATH)
print(loader)

text_documents= loader.load()

print(f"Number of documents: {len(text_documents)}")

for text_document in text_documents:
    print()
    print("-"*80)
    print()
    print("Type:", text_document.type)
    print("Metadata:", text_document.metadata)
    print()
    print(text_document.page_content)

#
# ---
#
# ### Documents handling - PDF documents loader
#
# - object initialization for loading PDF document
# - one text document loading and processing
# - print processed document metadata
# - print the returned document structure

from langchain_community.document_loaders import PyPDFLoader

DOCUMENT_PATH = "documents/EPL-2.0.pdf"

loader = PyPDFLoader(DOCUMENT_PATH)
print(loader)

pdf_documents= loader.load()

print(f"Number of documents: {len(pdf_documents)}")

for pdf_document in pdf_documents:
    print()
    print("-"*80)
    print()
    print("Type:", pdf_document.type)
    print("Metadata:", pdf_document.metadata)
    print()
    print(pdf_document.page_content)

#
# ---
#
# ### Documents handling - HTML pages loader
#
# - object initialization for loading HTML page or pages
# - one HTML page document loading and processing
# - print processed document metadata
# - print the returned document structure

from langchain_community.document_loaders import WebBaseLoader

DOCUMENT_URL = "https://www.eclipse.org/org/documents/epl-2.0/EPL-2.0.html"

loader = WebBaseLoader(DOCUMENT_URL)
print(loader)

text_documents= loader.load()

print(f"Number of documents: {len(text_documents)}")

for text_document in text_documents:
    print()
    print("-"*80)
    print()
    print("Type:", text_document.type)
    print("Metadata:", text_document.metadata)
    print()
    print(text_document.page_content)


#
# ---
#
# ### Document processing - chunking
#
# - object initialization for loading text document
# - one text document loading and processing
# - text chunking
# - print all chunks


from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

DOCUMENT_PATH = "documents/EPL-2.0.txt"

loader = TextLoader(DOCUMENT_PATH)
print(loader)

text_documents= loader.load()

text_splitter= RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks=text_splitter.split_documents(text_documents)

for chunk in chunks:
    print(chunk.page_content)
    print("-"*50)

#
# ---
#
# ### Document processing - chunking
#
# - object initialization for loading text document
# - one text document loading and processing
# - text chunking
# - print all chunks

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

DOCUMENT_PATH = "documents/assemblery.txt"

loader = TextLoader(DOCUMENT_PATH)
print(loader)
print()

text_documents= loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
splitted=text_splitter.split_documents(text_documents)

for chunk in splitted:
    print(chunk.page_content)
    print("-"*50)


#
# ---
#
# ### Document processing - chunking results
#
# - object initialization for loading text document
# - one text document loading and processing
# - text chunking
# - print all chunks
# - setting chung sizes

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

DOCUMENT_PATH = "documents/assemblery.txt"

loader = TextLoader(DOCUMENT_PATH)
print(loader)
print()

text_documents= loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=50)
splitted=text_splitter.split_documents(text_documents)

for chunk in splitted:
    print(chunk.page_content)
    print("-"*50)

#
# ---
#
# ### Document processing - overlapping chunks
#
# - object initialization for loading text document
# - one text document loading and processing
# - text chunking
# - print all chunks
# - setting chung sizes and overlap amount

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

DOCUMENT_PATH = "documents/assemblery.txt"

loader = TextLoader(DOCUMENT_PATH)
print(loader)
print()

text_documents= loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=100)
splitted=text_splitter.split_documents(text_documents)

for chunk in splitted:
    print(chunk.page_content)
    print("-"*50)

#
# ---
#
# # Vector databases
#
#    - specialized databases
#    - optimized for effective vector store
#    - optimized for effective vector search
#    - vector similarity search
#    - different metrics
#
#
# ## Vector distance
#    - Eukleidan metric
#    - cosine distance
#    - scalar product/dot product
#    - Manhattan metric
#
# * Vector database applications
#     - NLP
#     - image and voice recongition
#     - anomaly detection
#     - LLM
# 
# * Existing vector databases
#     - Aerospike
#     - AllegroGraph
#     - Apache Cassandra
#     - Azure Cosmos DB
#     - Chroma
#     - ClickHouse
#     - Couchbase
#     - CrateDB
#     - DataStax
#     - Elasticsearch
#     - HAKES
#     - HDF5 Query Indexing
#     - JaguarDB
#     - LanceDB
#     - Lantern
#     - LlamaIndex
#     - MariaDB
#     - Marqo
#     - Meilisearch
#     - Milvus
#     - MongoDB Atlas
#     - Neo4j
#     - ObjectBox
#     - OpenSearch
#     - Oracle Database
#     - Pinecone
#     - Pixeltable (Incremental Embedding)
#     - Postgres with pgvector
#     - Qdrant
#     - Redis Stack
#     - Snowflake
#     - SurrealDB
#     - Typesense
#     - Vespa
#     - Weaviate
# ---
#
# ## Embedding
#
# * Word embedding
#     - word -> vector
#     - similar words have small distacne
#     - word2vec Tomáš Mikolov
# * Sentence embedding
#     - the same, but for whole chunks
#     - this is why chunking is important
#
# ---
#
# ### Faiss
# 
# * Facebook AI Similarity Search
# * Open source
# * Support indexes
# * Vector search algorithms
# * Clustering algorithms
#
# ---
#
# ```
#                                │ y
#                                │
#                                │
#                                │
#                                │                [5,5]
#              o       o         │          o   o   o
#                                │          o   o   o
#                  o             │          o   o   o
#               [-4,3]           │        [3,3]   [5,3]
#                                │
# ─────────────────────────────[0,0]──────────────────────────────
#                                │                               x
#                                │              o
#                                │
#                                │          o       o
#                                │                [5,-5]
#                                │
#                                │
#                                │
#                                │
# ```
#

#
# ---
#
# ### How to define vectors? (simple way)
#
# - two vectors containing coordinates on plane
# - both vectors are printed
# - one vector with coordinates are constructed

x = [-5, -4, -3,    3,  4,  5,   3, 3, 3,  4, 4, 4,  5, 5, 5]

y = [ 5,  3,  5,   -5, -3, -5,   3, 4, 5,  3, 4, 5,  3, 4, 5]

print(x)
print(y)

print(list(zip(x, y)))

#
# ---
#
# ### Vectors in NumPy library
#
# - two list with coordinates
# - 2D matrix is constructed
# - matrix is printed

import numpy as np

x = [-5, -4, -3,    3,  4,  5,   3, 3, 3,  4, 4, 4,  5, 5, 5]

y = [ 5,  3,  5,   -5, -3, -5,   3, 4, 5,  3, 4, 5,  3, 4, 5]

points = np.column_stack((x,y)).astype("float32")

print(points)

#
# ---
#
# ### Index construction
#
# - index construction using FAISS
# - basic info about index is printed

import faiss
import numpy as np

x = [-5, -4, -3,    3,  4,  5,   3, 3, 3,  4, 4, 4,  5, 5, 5]

y = [ 5,  3,  5,   -5, -3, -5,   3, 4, 5,  3, 4, 5,  3, 4, 5]

points = np.column_stack((x,y)).astype("float32")
print(points)

index = faiss.IndexFlatL2(2)
index.add(points)

print()
print("Dimension(s):         ", index.d)
print("Total values in index:", index.ntotal)
print("Is index trained:     ", index.is_trained)

#
# ---
#
# ### Vector similarity search
#
# - based on FAISS
# - L2 metrics
# - list of most similar vectors

import faiss
import numpy as np

x = [-5, -4, -3,    3,  4,  5,   3, 3, 3,  4, 4, 4,  5, 5, 5]

y = [ 5,  3,  5,   -5, -3, -5,   3, 4, 5,  3, 4, 5,  3, 4, 5]

points = np.column_stack((x,y)).astype("float32")
print(points)

index = faiss.IndexFlatL2(2)
index.add(points)

print()
print("Dimension(s):         ", index.d)
print("Total values in index:", index.ntotal)
print("Is index trained:     ", index.is_trained)

query_vector = np.array([[3, 3]]).astype("float32")
print(query_vector)

k = len(x)

distances, indices = index.search(query_vector, k)

print("Nearest neighbors:")
print("neighbour  distance  index")
print("--------------------------")
for i in range(k):
    print(f"{i+1:3}      {distances[0][i]:5}       {indices[0][i]:2}")

#
# ```
# Nearest neighbors:
# neighbour  distance  index
# --------------------------
#   1        0.0        6
#   2        1.0        7
#   3        1.0        9
#   4        2.0       10
#   5        4.0        8
#   6        4.0       12
#   7        5.0       11
#   8        5.0       13
#   9        8.0       14
#  10       37.0        4
#  11       40.0        2
#  12       49.0        1
#  13       64.0        3
#  14       68.0        0
#  15       68.0        5
# ```
#

#
# ---
#
# ### Vector similarity search
#
# - based on FAISS
# - L2 metrics
# - list of most similar vectors

import faiss
import numpy as np

x = [-5, -4, -3,    3,  4,  5,   3, 3, 3,  4, 4, 4,  5, 5, 5]

y = [ 5,  3,  5,   -5, -3, -5,   3, 4, 5,  3, 4, 5,  3, 4, 5]

points = np.column_stack((x,y)).astype("float32")
print(points)

index = faiss.IndexFlatL2(2)
index.add(points)

print()
print("Dimension(s):         ", index.d)
print("Total values in index:", index.ntotal)
print("Is index trained:     ", index.is_trained)

query_vector = np.array([[3, 3]]).astype("float32")
print(query_vector)

k = len(x)

distances, indices = index.search(query_vector, k)

print("Nearest neighbors:")
print("neighbour  distance  coordinates  ")
print("----------------------------------")
for i in range(k):
    print(f"{i+1:3}      {distances[0][i]:5}       {points[indices[0][i]]}")

# ```
# Nearest neighbors:
# neighbour  distance  coordinates
# ----------------------------------
#   1        0.0       [3. 3.]
#   2        1.0       [3. 4.]
#   3        1.0       [4. 3.]
#   4        2.0       [4. 4.]
#   5        4.0       [3. 5.]
#   6        4.0       [5. 3.]
#   7        5.0       [4. 5.]
#   8        5.0       [5. 4.]
#   9        8.0       [5. 5.]
#  10       37.0       [ 4. -3.]
#  11       40.0       [-3.  5.]
#  12       49.0       [-4.  3.]
#  13       64.0       [ 3. -5.]
#  14       68.0       [-5.  5.]
#  15       68.0       [ 5. -5.]
# ```

# ---

# ### Three points that are closest to [-4, 4]

query_vector = np.array([[-4, 4]]).astype("float32")
print(query_vector)

k = 3
distances, indices = index.search(query_vector, k)

#
# ```
# Nearest neighbors:
# neighbour  distance  coordinates  
# ----------------------------------
#   1        1.0       [-4.  3.]
#   2        2.0       [-5.  5.]
#   3        2.0       [-3.  5.]
# ```
#
# ### Results visualization
#
# ```
#                                │ y
#                                │
#                                │
#                                │
#                                │
#              o       o         │          x   x   x
#                  *             │          x   x   x
#                  o             │          x   x   x
#                                │
#                                │
# ─────────────────────────────[0,0]──────────────────────────────
#                                │                               x
#                                │
#                                │              x
#                                │
#                                │          x       x
#                                │
#                                │
#                                │
#                                │
# ```

#
# ---
#
# ### Vector similarity based on FAISS
#
# - scalar product metric
# - prints most similar vectors
# - vectors are not normalized

import faiss
import numpy as np

x = [-5, -4, -3,    3,  4,  5,   3, 3, 3,  4, 4, 4,  5, 5, 5]

y = [ 5,  3,  5,   -5, -3, -5,   3, 4, 5,  3, 4, 5,  3, 4, 5]

points = np.column_stack((x,y)).astype("float32")
print(points)

index = faiss.IndexFlatIP(2)
index.add(points)

print()
print("Dimension(s):         ", index.d)
print("Total values in index:", index.ntotal)
print("Is index trained:     ", index.is_trained)

query_vector = np.array([[3, 3]]).astype("float32")
print(query_vector)

k = len(x)

distances, indices = index.search(query_vector, k)

print("Nearest neighbors:")
print("neighbour  distance  coordinates  ")
print("----------------------------------")
for i in range(k):
    print(f"{i+1:3}      {distances[0][i]:5}       {points[indices[0][i]]}")

#
# ---
#
# ### Vector similarity based on FAISS
#
# - scalar product metric
# - prints most similar vectors
# - vectors are normalized

import faiss
import numpy as np

x = [-5, -4, -3,    3,  4,  5,   3, 3, 3,  4, 4, 4,  5, 5, 5]

y = [ 5,  3,  5,   -5, -3, -5,   3, 4, 5,  3, 4, 5,  3, 4, 5]

points = np.column_stack((x,y)).astype("float32")
print(points)

for i in range(len(points)):
   vector = points[i]
   normalized = np.linalg.norm(vector)
   vector /= normalized
   points[i] = vector

print()
print("Normalized:")
print(points)

index = faiss.IndexFlatIP(2)
index.add(points)

print()
print("Dimension(s):         ", index.d)
print("Total values in index:", index.ntotal)
print("Is index trained:     ", index.is_trained)

query_vector = np.array([[3, 3]]).astype("float32")
normalized = np.linalg.norm(query_vector)
query_vector /= normalized
print(query_vector)

k = len(x)

distances, indices = index.search(query_vector, k)

print("Nearest neighbors:")
print("neighbour  distance  coordinates  ")
print("----------------------------------")
for i in range(k):
    print(f"{i+1:3}      {distances[0][i]:+7.4f}     {points[indices[0][i]]}")

#
# ---
#
# ### Benchmark
#
# - vector similarity search benchmark
# - results as table
# - visualization as a graph

from time import time

import faiss
import matplotlib.pyplot as plt
import numpy as np


def similarity_search(n, k):
    """Nalezeni k nejblizsich vektoru v mnozine n vektoru."""
    DIMENSIONS=128

    t1 = time()

    data = np.random.rand(n, 128).astype('float32')

    t2 = time()

    index = faiss.IndexFlatL2(DIMENSIONS)
    index.add(data)

    t3 = time()

    query_vector = np.random.rand(1, DIMENSIONS).astype("float32")

    distances, indices = index.search(query_vector, k)
    t4 = time()

    assert len(distances) == k
    assert len(indices) == k

    return n, t2-t1, t3-t2, t4-t3


ns = []
ts_rand = []
ts_index = []
ts_search = []

for n in np.linspace(1000000, 10000000, 10):
    print(n)
    n, t_rand, t_index, t_search = similarity_search(int(n), 1)
    ns.append(n)
    ts_rand.append(t_rand)
    ts_index.append(t_index)
    ts_search.append(t_search)


plt.plot(ns, ts_rand, "r-", label="numpy.random.rand")
plt.plot(ns, ts_index, "b-", label="index creation")
plt.plot(ns, ts_search, "m-", label="similarity search")

plt.legend(loc="upper left")

plt.grid(True)

plt.savefig("faiss_benchmark_2.png")

plt.show()

#
# ---
#
# ### Vector visualization on plane
#
# - vector endpoints are visualized

import matplotlib.pyplot as plt
import numpy as np

DIMENSIONS=2

N=1000

K=100

vectors = np.random.rand(N, DIMENSIONS).astype("float32")

plt.figure(figsize=(8, 8), dpi=80)

plt.plot(vectors[:,0], vectors[:,1], "+k", label="original vectors", markersize=5)

plt.legend(loc="upper left")

plt.grid(True)

plt.savefig("faiss-9.png")

plt.show()

#
# ---
#
# ### Vector visualization on plane
#
# - L2 metric
# - vectors are not normalized

import faiss
import matplotlib.pyplot as plt
import numpy as np

DIMENSIONS=2

N=1000

K=100

vectors = np.random.rand(N, DIMENSIONS).astype("float32")

index = faiss.IndexFlatL2(DIMENSIONS)
index.add(vectors)

query_vector = np.array([[0.5, 0.5]]).astype("float32")

distances, indices = index.search(query_vector, K)

plt.figure(figsize=(8, 8), dpi=80)

plt.plot(vectors[:,0], vectors[:,1], "+k", label="original vectors", markersize=5)

xs = vectors[:,0][indices][0]
ys = vectors[:,1][indices][0]
plt.plot(xs, ys, "+r", label="nearest vectors", markersize=5)

x = query_vector[0][0]
y = query_vector[0][1]
plt.plot(x, y, "ob", label="query vector", markersize=10)

plt.legend(loc="upper left")

plt.grid(True)

plt.savefig("faiss-A.png")

plt.show()




















# # PgVector
#
# * PostgreSQL database extension
# * New data type "vector"
# * Support multiple vector item types
# * New operators (vector distances)
#     - different metrics

# ```
# 
# Operator  Description
# -------------------------
# <->   Eucleidan distance
# <#>   dot product (scalar product)
# <=>   cosine between two vectors
# <+>   Manhattan metric
# <~>   Hammingon metric
# <%>   Jaccard index
# 
# ```

# ---
#
# ### Table construction containing vector columnt

import psycopg2

connection = psycopg2.connect(
    host="", port=5432, user="tester", password="123qwe", dbname="test"
)

print(connection)

CREATE_TABLE_STATEMENT = """
    CREATE TABLE IF NOT EXISTS v2 (
        id bigserial PRIMARY KEY,
        embedding vector(2) NOT NULL
    );
"""

LIST_TABLES_QUERY = """
    SELECT table_schema,table_name
      FROM information_schema.tables
     WHERE table_schema='public'
     ORDER BY table_schema,table_name;
"""

with connection.cursor() as cursor:
    print(CREATE_TABLE_STATEMENT)
    cursor.execute(CREATE_TABLE_STATEMENT)
    connection.commit()

    print(LIST_TABLES_QUERY)
    cursor.execute(LIST_TABLES_QUERY)
    tables = cursor.fetchall()

    for table in tables:
        print(table)

#
# ---
#
# ### Table construction - larger vectors

import psycopg2

connection = psycopg2.connect(
    host="", port=5432, user="tester", password="123qwe", dbname="test"
)

print(connection)

CREATE_TABLE_STATEMENT = """
    CREATE TABLE IF NOT EXISTS v384 (
        id bigserial PRIMARY KEY,
        embedding vector(384) NOT NULL
    );
"""

LIST_TABLES_QUERY = """
    SELECT table_schema,table_name
      FROM information_schema.tables
     WHERE table_schema='public'
     ORDER BY table_schema,table_name;
"""

with connection.cursor() as cursor:
    print(CREATE_TABLE_STATEMENT)
    cursor.execute(CREATE_TABLE_STATEMENT)
    connection.commit()

    print(LIST_TABLES_QUERY)
    cursor.execute(LIST_TABLES_QUERY)
    tables = cursor.fetchall()

    for table in tables:
        print(table)

#
# ---
#
# ### Table construction containing original texts

import psycopg2

connection = psycopg2.connect(
    host="", port=5432, user="tester", password="123qwe", dbname="test"
)

print(connection)

CREATE_TABLE_STATEMENT = """
    CREATE TABLE IF NOT EXISTS v384b (
        id bigserial PRIMARY KEY,
        embedding vector(384) NOT NULL,
        sentence TEXT NOT NULL
    );
"""

LIST_TABLES_QUERY = """
    SELECT table_schema,table_name
      FROM information_schema.tables
     WHERE table_schema='public'
     ORDER BY table_schema,table_name;
"""

with connection.cursor() as cursor:
    print(CREATE_TABLE_STATEMENT)
    cursor.execute(CREATE_TABLE_STATEMENT)
    connection.commit()

    print(LIST_TABLES_QUERY)
    cursor.execute(LIST_TABLES_QUERY)
    tables = cursor.fetchall()

    for table in tables:
        print(table)

#
# ---
#
# ### Fill-in table containing vector column

import psycopg2

import numpy as np
from pgvector.psycopg2 import register_vector

connection = psycopg2.connect(
    host="", port=5432, user="tester", password="123qwe", dbname="test"
)

register_vector(connection)

x = [-5, -4, -3,    3,  4,  5,   3, 3, 3, 4, 4, 4, 5, 5, 5]
y = [ 5,  3,  5,   -5, -3, -5,   3, 4, 5, 3, 4, 5, 3, 4, 5]

with connection.cursor() as cursor:
    for i in range(len(x)):
        vector = np.array([x[i], y[i]])
        print(type(vector), vector)
        cursor.execute("INSERT INTO v2 (embedding) VALUES (%s)", (vector, ))
    connection.commit()


#
# ---
#
# ### Vector selection based on vector distance
#

import psycopg2

from pgvector.psycopg2 import register_vector

connection = psycopg2.connect(
    host="", port=5432, user="tester", password="123qwe", dbname="test"
)

register_vector(connection)

with connection.cursor() as cursor:
    cursor.execute("SELECT embedding FROM v2 ORDER BY embedding <-> %s::vector LIMIT 5", ([3,3], ))
    records = cursor.fetchall()
    for record in records:
        print(record[0])

#
# ---
#
# ### Vector selection based on vector distance
#

import psycopg2

from pgvector.psycopg2 import register_vector

connection = psycopg2.connect(
    host="", port=5432, user="tester", password="123qwe", dbname="test"
)

register_vector(connection)

query = """
    SELECT embedding
      FROM v2
     WHERE embedding <-> %s::vector < %s
"""

for distance in range(0, 10):
    print("Distance:", distance)
    with connection.cursor() as cursor:
        cursor.execute(query, ([3,3], distance))
        records = cursor.fetchall()
        for record in records:
            print(record[0])
    print("-"*50)

#
# ---
#
# ### Other operators available

import psycopg2

from pgvector.psycopg2 import register_vector

connection = psycopg2.connect(
    host="", port=5432, user="tester", password="123qwe", dbname="test"
)

register_vector(connection)


def list_by_distance(title, query):
    print(title)
    print("-" * 70)
    with connection.cursor() as cursor:
        cursor.execute(query, ([3,3], ))
        records = cursor.fetchall()
        for record in records:
            print(record[0], record[1])
    print()


query_l2_distance = """
        SELECT embedding, embedding <-> %s::vector as distance
          FROM v2
         ORDER BY distance
    """


query_cosine_distance = """
        SELECT embedding, embedding <=> %s::vector as distance
          FROM v2
         ORDER BY distance
    """


query_inner_product_distance = """
        SELECT embedding, (embedding <#> %s::vector) * -1 as distance
          FROM v2
         ORDER BY distance
    """


list_by_distance("L2", query_l2_distance)
list_by_distance("cosine", query_cosine_distance)
list_by_distance("inner product", query_inner_product_distance)

#
# ---
#
# ### Table containing binary vectors
#

import psycopg2

connection = psycopg2.connect(
    host="localhost", port=54321, user="tester", password="123qwe", dbname="test"
)

print(connection)

CREATE_TABLE_STATEMENT = """
    CREATE TABLE IF NOT EXISTS b1 (
        id bigserial PRIMARY KEY,
        embedding bit (4) NOT NULL
    );
"""

LIST_TABLES_QUERY = """
    SELECT table_schema,table_name
      FROM information_schema.tables
     WHERE table_schema='public'
     ORDER BY table_schema,table_name;
"""

with connection.cursor() as cursor:
    print(CREATE_TABLE_STATEMENT)
    cursor.execute(CREATE_TABLE_STATEMENT)
    connection.commit()

    print(LIST_TABLES_QUERY)
    cursor.execute(LIST_TABLES_QUERY)
    tables = cursor.fetchall()

    for table in tables:
        print(table)

#
# ---
#
# ### Inserting data into table with binary vectors
#

import psycopg2

import numpy as np
from pgvector.psycopg2 import register_vector

connection = psycopg2.connect(
    host="localhost", port=54321, user="tester", password="123qwe", dbname="test"
)

register_vector(connection)

vectors = [
        "0000",
        "1111",
        "1100",
        "0011",
        ]

with connection.cursor() as cursor:
    for vector in vectors:
        cursor.execute("INSERT INTO b1 (embedding) VALUES (%s)", (vector, ))
    connection.commit()


#
# ---
#
# ### Vector distance operators and table containing binary vectors
#

import psycopg2

from pgvector.psycopg2 import register_vector

connection = psycopg2.connect(
    host="localhost", port=54321, user="tester", password="123qwe", dbname="test"
)

register_vector(connection)

with connection.cursor() as cursor:
    cursor.execute("SELECT embedding FROM b1 ORDER BY embedding <~> %s::bit(4) LIMIT 5", ("0100", ))
    records = cursor.fetchall()
    for record in records:
        print(record[0])

#
# ---
#
# ### Vector distance operators and table containing binary vectors
#

import psycopg2

from pgvector.psycopg2 import register_vector

connection = psycopg2.connect(
    host="localhost", port=54321, user="tester", password="123qwe", dbname="test"
)

register_vector(connection)

with connection.cursor() as cursor:
    cursor.execute("SELECT embedding, embedding <~> '0000' AS distance FROM b1 ORDER BY distance")
    records = cursor.fetchall()
    for record in records:
        print(record[0], record[1])

#
# ---
#
# # SentenceTransformer
#

# ---
#
# ### Embedding model initialization
#
# - commonly used model

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("paraphrase-MiniLM-L6-v2")

print(model)

#
# ---
#
# ### Embedding model initialization
#
# - different model is used

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-mpnet-base-v2")

print(model)

#
# ---
#
# ### It is possible to use models for different languages
#
# - can be used in the same style as English models

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("Seznam/small-e-czech")

print(model)

#
# ---
#
# ### Sentence vectorization
#
# - output vectors are based on model used

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("paraphrase-MiniLM-L6-v2")

print(model)

sentences = [
    "The rain in Spain falls mainly on the plain",
    "The tesselated polygon is a special type of polygon",
    "The quick brown fox jumps over the lazy dog",
    "To be or not to be, that is the question",
    "It is a truth universally acknowledged...",
    "The goat ran down the hill"
]

embeddings = model.encode(sentences)
print(f"Embeddings shape: {embeddings.shape}")

print(f"Data type: {type(embeddings)}")

print(embeddings)

np.info(embeddings)

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

