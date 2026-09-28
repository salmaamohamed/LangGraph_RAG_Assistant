from state import Document, RAGState


def web_search(state: RAGState) -> dict:
	question = state["question"]
	results: list[Document] = []
	api_key = __import__("config").TAVILY_API_KEY
	if api_key:
		try:
			from tavily import TavilyClient

			response = TavilyClient(api_key=api_key).search(query=question, max_results=3)
			results = [
				{"title": item.get("title", "Web result"), "content": item.get("content", ""), "source": item.get("url", "")}
				for item in response.get("results", [])
			]
		except Exception:
			results = []
	if not results:
		results = [{
			"title": "Web search fallback",
			"source": "web://fallback",
			"content": f"No live search provider is configured. The assistant searched for: {question}. Answer only what can be established from this search context.",
		}]
	return {
		"web_results": results,
		"sources": [result["source"] for result in results],
		"trace": state.get("trace", []) + [f"web_search:{len(results)}"],
	}
