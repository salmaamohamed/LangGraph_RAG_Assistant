from state import RAGState
from rag.vectorstore import search_documents


def route_question(state: RAGState) -> dict:
	question = state["question"]
	route = "local" if search_documents(question, limit=1) else "web"
	trace = state.get("trace", []) + [f"route_question:{route}"]
	return {"route": route, "trace": trace}
