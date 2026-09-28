from typing import TypedDict


class Document(TypedDict):
	title: str
	content: str
	source: str


class RAGState(TypedDict, total=False):
	question: str
	documents: list[Document]
	web_results: list[Document]
	generation: str
	route: str
	document_grade: str
	answer_grade: str
	retries: int
	max_retries: int
	sources: list[str]
	trace: list[str]
