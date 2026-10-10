
from pathlib import Path
from app.core.config import get_settings
from app.services.ingestion import load_file, chunk_documents
from app.rag.vectorstore import add_documents

settings = get_settings()

folder= Path(settings.sample_kb_dir)
files=[f for f in folder.iterdir() if f.is_file()]

all_docs = []
for path in files:
    all_docs.extend(load_file(path))
    chunk_docs = chunk_documents(all_docs)
    add_documents(chunk_docs)