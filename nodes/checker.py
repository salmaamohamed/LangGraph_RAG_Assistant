from state import RAGState


def check_answer(state: RAGState) -> dict:
	answer = state.get("generation", "")
	supported = bool(state.get("documents") or state.get("web_results")) and len(answer) > 60
	grade = "supported" if supported else "unsupported"
	retries = state.get("retries", 0) + (0 if supported else 1)
	return {
		"answer_grade": grade,
		"retries": retries,
		"trace": state.get("trace", []) + [f"check_answer:{grade}"],
	}
