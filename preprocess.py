import json
from pathlib import Path
from typing import Any

from sklearn.feature_extraction.text import TfidfVectorizer

from services.nlp_service import NLPService


class Preprocessor:
    def __init__(self, dataset: str) -> None:
        self.dataset = Path(dataset)
        self.questions: list[str] = []
        self.answers: list[str] = []
        self.vectorizer = TfidfVectorizer()
        self.nlp_service = NLPService()
        self.load_data()

    def clean(self, text: str) -> str:
        return self.nlp_service.clean(text)

    def load_data(self) -> None:
        with self.dataset.open(encoding="utf-8") as file:
            data: Any = json.load(file)

        if not isinstance(data, list):
            raise ValueError("The FAQ dataset must contain a list of entries.")

        for item in data:
            if not isinstance(item, dict):
                raise ValueError("Each FAQ entry must be an object.")

            question = item.get("question")
            answer = item.get("answer")
            if not isinstance(question, str) or not isinstance(answer, str):
                raise ValueError("Each FAQ entry needs string question and answer values.")

            self.questions.append(self.clean(question))
            self.answers.append(answer)

        self.matrix = self.vectorizer.fit_transform(self.questions)
