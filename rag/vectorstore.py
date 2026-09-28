from pathlib import Path
import re

from state import Document

_DOCUMENTS: list[Document] = [
	{
		"title": "LangGraph fundamentals",
		"source": "local://langgraph-fundamentals",
		"content": "LangGraph is a framework for building stateful, multi-step applications with language models. A graph contains nodes, edges, conditional edges, and a shared state. START begins execution and END terminates it.",
	},
	{
		"title": "Adaptive RAG workflow",
		"source": "local://adaptive-rag",
		"content": "An adaptive RAG assistant routes a question to a local knowledge base or web search. A document grader checks retrieved relevance. If documents are useful, generation uses them; otherwise the workflow searches the web.",
	},
	{
		"title": "LangGraph state and loops",
		"source": "local://state-and-loops",
		"content": "LangGraph state is shared between nodes and records values such as the question, documents, answer, sources, and retry count. Conditional edges can send an execution back to a node, creating a controlled loop.",
	},
	{
		"title": "Retrieval augmented generation",
		"source": "local://rag",
		"content": "Retrieval augmented generation retrieves relevant context before producing an answer. Grounded answers should cite the context they used and should avoid unsupported claims.",
	},
]


_STOP_WORDS = {
	"about", "after", "and", "are", "does", "for", "from", "how", "into",
	"that", "the", "this", "what", "when", "where", "which", "with",
}


def _terms(text: str) -> set[str]:
	return {
		word for word in re.findall(r"[a-zA-Z0-9]+", text.lower())
		if len(word) > 2 and word not in _STOP_WORDS
	}


def load_documents() -> list[Document]:
	return list(_DOCUMENTS)


def search_documents(query: str, limit: int = 3) -> list[Document]:
	query_terms = _terms(query)
	scored = []
	for document in _DOCUMENTS:
		document_terms = _terms(document["title"] + " " + document["content"])
		score = len(query_terms & document_terms)
		if score:
			scored.append((score, document))
	scored.sort(key=lambda item: item[0], reverse=True)
	return [document for _, document in scored[:limit]]
