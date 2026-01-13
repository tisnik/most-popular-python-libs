# Framework LangChain
#
# - inicializace objektu pro načítání textových dokumentů
# - načtení a zpracování jednoho textového dokumentu
# - tisk obsahu objektu představujícího dokument

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
