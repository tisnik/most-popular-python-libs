# Framework LangChain
#
# - inicializace objektu pro načítání textových dokumentů
# - načtení a zpracování jednoho textového dokumentu
# - rozdělení dokumentu do menších částí
# - tisk všech částí dokumentu
# - nastavení velikosti jednotlivých částí a velikosti překryvu

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
