import json
import os
from datetime import datetime

HISTORY_FILE = "history/chat_history.json"


class HistoryService:
    def __init__(self) -> None:
        self.history_file = HISTORY_FILE

    def _ensure_file(self) -> None:
        """Create history file if it doesn't exist."""
        os.makedirs("history", exist_ok=True)

        if not os.path.exists(self.history_file):
            with open(self.history_file, "w", encoding="utf-8") as file:
                json.dump([], file, indent=4)

    def load(self) -> list[dict[str, str]]:
        """Load complete chat history."""
        self._ensure_file()

        with open(self.history_file, "r", encoding="utf-8") as file:
            return json.load(file)

    def save(self, question: str, answer: str) -> None:
        """Save one chat conversation."""
        self._ensure_file()

        history = self.load()
        history.append(
            {
                "question": question,
                "answer": answer,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        )

        with open(self.history_file, "w", encoding="utf-8") as file:
            json.dump(history, file, indent=4)

    def clear(self) -> None:
        """Delete all history."""
        self._ensure_file()

        with open(self.history_file, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)

    def total_chats(self) -> int:
        """Return total number of chats."""
        history = self.load()
        return len(history)


def _ensure_file():
    """Create history file if it doesn't exist."""
    os.makedirs("history", exist_ok=True)

    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)


def load_history():
    """Load complete chat history."""
    return HistoryService().load()


def save_chat(question, answer):
    """Save one chat conversation."""
    HistoryService().save(question, answer)


def clear_history():
    """Delete all history."""
    HistoryService().clear()


def total_chats():
    """Return total number of chats."""
    return HistoryService().total_chats()
