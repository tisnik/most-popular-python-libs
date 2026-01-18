# Framework LangChain
#
# - inicializace objektu pro načítání obsahu HTML stránek
# - načtení a zpracování jedné HTML stránky
# - tisk typu dokumentu a metadat
# - tisk obsahu objektu představujícího dokument

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
