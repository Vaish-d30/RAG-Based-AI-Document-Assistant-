from typing import List, Dict, Any
from vector_store import VectorStore, vectorstore 
from embeddings import EmbeddingManager,embedding_manager

class RAGRetriever:
    """Retrieves relevant documents from the vector store based on a query"""

    def __init__(self, vector_store: VectorStore, embedding_manager: EmbeddingManager):
        self.vector_store = vector_store
        self.embedding_manager = embedding_manager

    def retrieve(self, query: str, top_k: int = 5, score_threshold: float = 0.0) -> List[Dict[str, Any]]:

        print(f"Retrieving documents for query: '{query}'")
        print(f"Top K: {top_k}, Score Threshold: {score_threshold}")

        # Generate query embedding
        query_embedding = self.embedding_manager.generate_embeddings([query])[0]

        try:
            results = self.vector_store.collection.query(
                query_embeddings=[query_embedding.tolist()],
                n_results=top_k,
                include=["documents", "metadatas", "distances"]   # FIXED
            )

            retrieved_docs = []

            if results and results.get("documents") and results["documents"][0]:

                documents = results["documents"][0]
                metadatas = results["metadatas"][0]
                distances = results["distances"][0]
                ids = results["ids"][0]  # ids come automatically

                for doc_id, document, metadata, distance in zip(ids, documents, metadatas, distances):

                    similarity_score = 1 - distance

                    if similarity_score >= score_threshold:
                        retrieved_docs.append({
                            "id": doc_id,
                            "document": document,
                            "metadata": metadata,
                            "similarity_score": similarity_score
                        })

                print(f"Retrieved {len(retrieved_docs)} documents above the score threshold")

            else:
                print("No documents retrieved for the query.")

            return retrieved_docs

        except Exception as e:
            print(f"Error retrieving documents: {e}")
            return []
        
# Initialize RAG retriever
rag_retriever = RAGRetriever(vectorstore, embedding_manager)

rag_retriever
