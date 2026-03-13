import google.generativeai as genai
import os
from dotenv import load_dotenv
from retriever import rag_retriever

load_dotenv()
# Initialize Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

llm = genai.GenerativeModel("gemini-2.5-flash")


def enhanced_rag(query, retriever, llm, top_k=5, debug=False):
    """
    Enhanced RAG pipeline:
    Retrieval → Context Ranking → Prompt Engineering → LLM Response
    """

    # STEP 1: Retrieve documents
    results = retriever.retrieve(query, top_k=top_k)
    
    if not results:
    return {
        "answer": "No relevant documents found.",
        "sources": []
    }

    # STEP 2: Sort by similarity score (best first)
    results = sorted(results, key=lambda x: x["similarity_score"], reverse=True)

    # STEP 3: Build context
    context_chunks = []
    sources = []

    for r in results:
        context_chunks.append(r["document"])
        sources.append(r["metadata"].get("source", "unknown"))

    context = "\n\n".join(context_chunks)

    if debug:
        print("\nRetrieved Context:")
        for r in results:
            print(f"Score: {r['similarity_score']:.3f}")

    # STEP 4: Better prompt
    prompt = f"""
You are an AI assistant answering questions using retrieved documents.

Rules:
- Only answer using the provided context.
- If the answer is not in the context, say "The answer is not found in the provided documents."
- Keep answers concise and clear.

Context:
{context}

Question:
{query}

Answer:
"""

    # STEP 5: Generate response
    response = llm.generate_content(prompt)

    answer = response.text.strip()

    return {
        "answer": answer,
        "sources": list(set(sources))
    }



