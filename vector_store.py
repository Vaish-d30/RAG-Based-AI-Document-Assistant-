import os
import uuid
import chromadb
from data_ingestion import documents
from embeddings import embedding_manager
import numpy as np
from typing import List, Any


class VectorStore:
    """Manages document embeddings in a ChromaDB vector store"""

    def __init__(self, collection_name: str = "pdf_documents", persist_directory: str = "chroma_db"):
        """
        Initialize the vector store

        Args:
            collection_name (str): Name of the collection in ChromaDB
            persist_directory (str): Directory to persist vector database
        """

        self.collection_name = collection_name
        self.persist_directory = persist_directory
        self.client = None
        self.collection = None

        self._initialize_store()

    def _initialize_store(self):
        """Initialize the ChromaDB client and collection"""

        try:
            os.makedirs(self.persist_directory, exist_ok=True)

            # New ChromaDB persistent client (correct modern syntax)
            self.client = chromadb.PersistentClient(path=self.persist_directory)

            self.collection = self.client.get_or_create_collection(
                name=self.collection_name,
                metadata={"description": "Collection of PDF document embeddings"}
            )

            print("ChromaDB client and collection initialized successfully")

        except Exception as e:
            print(f"Error initializing ChromaDB: {e}")
            raise e

    def add_documents(self, documents: List[Any], embeddings: np.ndarray):
        """
        Add documents and their embeddings to the vector store

        Args:
            documents (List[Any]): List of document objects
            embeddings (np.ndarray): Corresponding embeddings
        """

        if len(documents) != len(embeddings):
            raise ValueError("Number of documents and embeddings must match")

        print(f"Adding {len(documents)} documents to the vector store...")

        ids = []
        metadatas = []
        documents_texts = []
        embeddings_list = []

        for i, (doc, embedding) in enumerate(zip(documents, embeddings)):

            # Unique ID
            doc_id = f"doc_{uuid.uuid4().hex[:8]}_{i}"
            ids.append(doc_id)

            # Metadata
            metadata = dict(doc.metadata)
            metadata["doc_index"] = i
            metadata["content_length"] = len(doc.page_content)

            metadatas.append(metadata)

            # Document content
            documents_texts.append(doc.page_content)

            # Convert numpy embedding to list
            embeddings_list.append(embedding.tolist())

        try:
            self.collection.add(
                ids=ids,
                documents=documents_texts,
                metadatas=metadatas,
                embeddings=embeddings_list
            )

            print("Documents added to vector store successfully")

        except Exception as e:
            print(f"Error adding documents to vector store: {e}")
            raise e


# Initialize vector store
vectorstore = VectorStore()

print(vectorstore)

# Convert documents to text and generate embeddings
documents_texts = [doc.page_content for doc in documents]
embeddings = embedding_manager.generate_embeddings(documents_texts)

# Add documents and embeddings to vector store

vectorstore.add_documents(documents, embeddings)
