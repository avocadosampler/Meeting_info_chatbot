from flask import Flask, render_template, request, jsonify

from utils.document_loader import list_documents, load_document
from utils.chunker import chunk_text
from utils.retriever import retrieve_chunks, add_to_index
from utils.ingest import sync_database
from utils.llm import call_llm

app = Flask(__name__)

# -----------------------------
# Routes
# -----------------------------

@app.route("/")
def index():
    docs = list_documents()
    return render_template("index.html", documents=docs)


@app.route("/documents")
def documents():
    return jsonify({"documents": list_documents()})


@app.route("/documents/<doc_name>")
def document_content(doc_name):
    try:
        text = load_document(doc_name)
        return jsonify({"document": doc_name, "content": text})
    except FileNotFoundError:
        return jsonify({"error": "Document not found"}), 404

# TO DO - CREATE THE CHATTING INTERFACE FUNCTION BELOW
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    query = data.get("query", "")
    
    if not query:
        return jsonify({"error": "Query is empty"}), 400

    # 1. RETRIEVAL: Query ChromaDB directly
    # (Assuming you've already run add_to_index for your files)
    context = retrieve_chunks(query)

    # 2. AUGMENTATION
    prompt = f"Using the context below, answer the question.\nContext: {context}\nQuestion: {query}"

    # 3. GENERATION
    answer = call_llm(prompt)

    return jsonify({"query": query, "answer": answer})

if __name__ == "__main__":
    sync_database()
    app.run(debug=True)
