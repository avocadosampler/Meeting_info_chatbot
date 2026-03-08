# Document RAG Application

A Flask-based Retrieval-Augmented Generation (RAG) application that indexes .docx documents and enables intelligent question-answering using ChromaDB for vector search and OpenRouter for LLM responses.

## Features

- Document ingestion from .docx files
- Text chunking with configurable overlap
- Vector-based semantic search using ChromaDB
- LLM-powered question answering via OpenRouter (Google Gemini 2.5 Flash)
- Web interface for document browsing and chat

## Prerequisites

- Python 3.8+
- OpenRouter API key
- .docx documents to index

## Installation

1. Clone the repository and navigate to the project directory

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Install additional required packages:
```bash
pip install chromadb python-dotenv
```

## Configuration

1. Create a `.env` file in the project root:
```
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

2. Update the transcripts directory path in `utils/document_loader.py`:
```python
TRANSCRIPTS_DIR = Path(r"path/to/your/documents")
```
Replace with the absolute path to your folder containing .docx files.

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

The application will:
- Automatically index all .docx files from the configured directory
- Start the web server on `http://127.0.0.1:5000`

2. Open your browser and navigate to `http://127.0.0.1:5000`

## Usage

### Web Interface

- View all indexed documents on the home page
- Use the chat interface to ask questions about your documents
- The system retrieves relevant context and generates answers using the LLM

### API Endpoints

- `GET /` - Home page with document list
- `GET /documents` - JSON list of available documents
- `GET /documents/<doc_name>` - Get content of a specific document
- `POST /chat` - Submit a query and receive an AI-generated answer
  ```json
  {
    "query": "Your question here"
  }
  ```

## How It Works

1. **Ingestion**: Documents are loaded, split into chunks (1000 chars with 100 char overlap)
2. **Indexing**: Chunks are stored in ChromaDB with embeddings
3. **Retrieval**: User queries search for the 3 most relevant chunks
4. **Generation**: Retrieved context is sent to the LLM to generate an answer

## Project Structure

```
.
├── app.py                  # Flask application and routes
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (create this)
├── static/
│   └── style.css          # Styling
├── templates/
│   └── index.html         # Web interface
└── utils/
    ├── document_loader.py # Document loading from filesystem
    ├── chunker.py         # Text chunking logic
    ├── retriever.py       # ChromaDB integration
    ├── ingest.py          # Document indexing pipeline
    └── llm.py             # OpenRouter LLM integration
```

## Customization

- **Chunk size**: Modify `chunk_size` and `overlap` in `utils/chunker.py`
- **LLM model**: Change `LLM_MODEL` in `utils/llm.py`
- **Retrieval count**: Adjust `n_results` in the `/chat` route
- **Temperature**: Modify `temperature` in `utils/llm.py` for response creativity

## Troubleshooting

- **FileNotFoundError**: Verify the `TRANSCRIPTS_DIR` path in `utils/document_loader.py`
- **API errors**: Check your OpenRouter API key in `.env`
- **No results**: Ensure documents are properly indexed on startup
- **Import errors**: Install missing dependencies with `pip install <package>`

## Notes

- The application uses an in-memory ChromaDB instance (data is lost on restart)
- Debug mode is enabled by default (disable for production)
- Only .docx files are supported for document ingestion
