# from app.core.config import get_settings

# settings = get_settings()

# print(f"App Name: {settings.app_name}")
# print(f"App Environment: {settings.app_env}")
# print(f"OpenAI API Key: {settings.openai_api_key}")

from app.services.ingestion import load_file, chunk_documents
from pathlib import Path
from app.rag.vectorstore import add_documents

docs = load_file(Path("data/sample_kb/company_it_handbook.md"))
chunk_docs = chunk_documents(docs)

add_documents(chunk_docs)
