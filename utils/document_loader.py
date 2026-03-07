from pathlib import Path
from docx import Document

#1.  Using Path, create a directory of transcripts
# code here
TRANSCRIPTS_DIR = Path(r"C:\Users\chris\Documents\df-frontier\llms_build\transcripts")


#2. Create a function called list_documents()
# Fetching the .name of files from your directory
# HINT: Specifically look for files "looking like" .docx - with .glob()
# code here
def list_documents():       
    files = list(TRANSCRIPTS_DIR.glob('*.docx'))
    return files

# 3. Using exists, create an exception to handle the situation
# HINT: There is a .exists() method to help with this + raise error
def load_document(doc_name):
    doc_path = TRANSCRIPTS_DIR / doc_name
    # code here
    if not doc_path.exists():
        raise FileNotFoundError("No such file in directory")
    else:
        doc = Document(doc_path)
        paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
        return "\n".join(paragraphs)
    