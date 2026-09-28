from collections import Counter
import re


def tokenize(text: str) -> list[str]:
	return re.findall(r"[a-zA-Z0-9]+", text.lower())


def lexical_similarity(left: str, right: str) -> float:
	left_counts = Counter(tokenize(left))
	right_counts = Counter(tokenize(right))
	common = sum((left_counts & right_counts).values())
	return common / max(1, len(left_counts))
