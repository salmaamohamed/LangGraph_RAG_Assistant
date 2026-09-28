from state import RAGState
from rag.embeddings import lexical_similarity


def grade_documents(state: RAGState) -> dict:
	question = state["question"]
	documents = state.get("documents", [])
	relevant = any(lexical_similarity(question, document["content"]) >= 0.15 for document in documents)
	grade = "relevant" if relevant else "irrelevant"
	return {"document_grade": grade, "trace": state.get("trace", []) + [f"grade_documents:{grade}"]}
