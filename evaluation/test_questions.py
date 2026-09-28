from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import ask


QUESTIONS = [
	"What is LangGraph?",
	"How does shared state work in LangGraph?",
	"What are conditional edges?",
	"Explain retrieval augmented generation.",
	"What is the population of Egypt today?",
	"Who won the latest football world cup?",
	"What is the weather in Cairo?",
	"How can a graph avoid infinite retry loops?",
]


def run_evaluation() -> None:
	for number, question in enumerate(QUESTIONS, start=1):
		result = ask(question)
		print(f"{number}. {question}")
		print(f"   answer: {result['generation'][:160]}")
		print(f"   path: {' -> '.join(result['trace'])}")
		print()


if __name__ == "__main__":
	run_evaluation()
