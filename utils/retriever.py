import chromadb
from chromadb import Documents, EmbeddingFunction, Embeddings

client = chromadb.Client()

collection = client.get_or_create_collection(
    name = "documents"
    )



def add_to_index(doc_name, chunks):
    

    ids = [f"{doc_name}_{i}" for i in range(len(chunks))]
    metadatas = [{"source": doc_name} for _ in chunks]
    
    collection.add(
        documents=chunks,
        metadatas=metadatas,
        ids=ids
    )

def retrieve_chunks(query, n_results=3):
    """
    Search ChromaDB for the most relevant snippets.
    """
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    
    # Extract the text from the results
    retrieved_texts = results['documents'][0]
    return "\n---\n".join(retrieved_texts)