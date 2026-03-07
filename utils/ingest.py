from utils.document_loader import list_documents, load_document
from utils.chunker import chunk_text
from utils.retriever import add_to_index

def sync_database():
    docs = list_documents() # Get the list of .docx files
    for doc_path in docs:
        print(f"Indexing {doc_path}...")
        text = load_document(doc_path.name)
        chunks = chunk_text(text)
        add_to_index(doc_path.name, chunks)
