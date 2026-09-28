from state import RAGState


def generate_answer(state: RAGState) -> dict:
	context = state.get("documents", []) + state.get("web_results", [])
	if context:
		excerpts = " ".join(document["content"] for document in context[:3])
		answer = f"Based on the available sources, {excerpts}"
		sources = state.get("sources", []) + [document["source"] for document in state.get("documents", [])]
	else:
		answer = "I could not find supporting information for that question."
		sources = state.get("sources", [])
	return {
		"generation": answer,
		"sources": list(dict.fromkeys(sources)),
		"trace": state.get("trace", []) + ["generate_answer"],
	}
