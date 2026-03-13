import os
from langchain_community.document_loaders import PyPDFLoader, PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pathlib import Path

def process_all_pdfs():
    """Process all PDF files in the RAG project pdf_directory"""

    all_documents = []
    pdf_dir = Path("data")

    # Find all PDF files recursively
    pdf_files = list(pdf_dir.glob("**/*.pdf"))

    print(f"Found {len(pdf_files)} PDF files to process")

    for pdf_file in pdf_files:
        print(f"Processing {pdf_file}")
        try:
            # Load the PDF using PyMuPDFLoader
            loader = PyMuPDFLoader(str(pdf_file))
            documents = loader.load()

            # Split the documents into smaller chunks
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )

            split_docs = text_splitter.split_documents(documents)

            all_documents.extend(split_docs)

        except Exception as e:
            print(f"Error processing {pdf_file}: {e}")

    return all_documents


# Run the function
documents = process_all_pdfs()

print(f"Total chunks created: {len(documents)}")
