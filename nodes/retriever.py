from state import RAGState
from rag.vectorstore import search_documents


def retrieve_documents(state: RAGState) -> dict:
	documents = search_documents(state["question"])
	return {
		"documents": documents,
		"trace": state.get("trace", []) + [f"retrieve_documents:{len(documents)}"],
	}
