from graph import graph
from config import MAX_RETRIES


def ask(question: str) -> dict:
	result = graph.invoke({
		"question": question,
		"retries": 0,
		"max_retries": MAX_RETRIES,
		"documents": [],
		"web_results": [],
		"sources": [],
		"trace": [],
	})
	return result


if __name__ == "__main__":
	question = input("Question: ").strip()
	if question:
		result = ask(question)
		print(f"\nAnswer: {result['generation']}\n")
		print(f"Sources: {', '.join(result.get('sources', []))}")
		print(f"Path: {' -> '.join(result.get('trace', []))}")
