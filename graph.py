from langgraph.graph import END, START, StateGraph

from config import MAX_RETRIES
from nodes.checker import check_answer
from nodes.generator import generate_answer
from nodes.grader import grade_documents
from nodes.retriever import retrieve_documents
from nodes.router import route_question
from nodes.web_search import web_search
from state import RAGState


def _route_after_question(state: RAGState) -> str:
	return state["route"]


def _route_after_documents(state: RAGState) -> str:
	return "generate" if state["document_grade"] == "relevant" else "web_search"


def _route_after_answer(state: RAGState) -> str:
	if state["answer_grade"] == "supported" or state.get("retries", 0) >= state.get("max_retries", MAX_RETRIES):
		return "finish"
	return "retry"


def build_graph():
	workflow = StateGraph(RAGState)
	workflow.add_node("route_question", route_question)
	workflow.add_node("retrieve_documents", retrieve_documents)
	workflow.add_node("grade_documents", grade_documents)
	workflow.add_node("web_search", web_search)
	workflow.add_node("generate_answer", generate_answer)
	workflow.add_node("check_answer", check_answer)

	workflow.add_edge(START, "route_question")
	workflow.add_conditional_edges(
		"route_question",
		_route_after_question,
		{"local": "retrieve_documents", "web": "web_search"},
	)
	workflow.add_edge("retrieve_documents", "grade_documents")
	workflow.add_conditional_edges(
		"grade_documents",
		_route_after_documents,
		{"generate": "generate_answer", "web_search": "web_search"},
	)
	workflow.add_edge("web_search", "generate_answer")
	workflow.add_edge("generate_answer", "check_answer")
	workflow.add_conditional_edges(
		"check_answer",
		_route_after_answer,
		{"finish": END, "retry": "web_search"},
	)
	return workflow.compile()


graph = build_graph()
