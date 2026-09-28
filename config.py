import os

from dotenv import load_dotenv

load_dotenv()

MAX_RETRIES = int(os.getenv("MAX_RETRIES", "1"))
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


def has_openai() -> bool:
	return bool(os.getenv("OPENAI_API_KEY"))
