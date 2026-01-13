# Framework LangChain
#
# - inicializace objektu pro načítání dokumentů ve formátu PDF
# - načtení a zpracování jednoho dokumentu ve formátu PDF
# - tisk typu dokumentu a metadat
# - tisk obsahu objektu představujícího dokument

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

