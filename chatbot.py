from typing import TypedDict

from sklearn.metrics.pairwise import cosine_similarity

from preprocess import Preprocessor


class ChatbotResponse(TypedDict):
    answer: str
    confidence: float
    matched_question: str | None


class AIChatbot:
    def __init__(self, dataset: str = "faq_dataset.json") -> None:
        self.engine = Preprocessor(dataset)

    def get_response(self, question: str) -> ChatbotResponse:
        cleaned_question = self.engine.clean(question)
        vector = self.engine.vectorizer.transform([cleaned_question])
        similarity = cosine_similarity(vector, self.engine.matrix)

        score = float(similarity.max())
        index = int(similarity.argmax())

        if score < 0.30:
            return {
                "answer": "Sorry, I couldn't find a relevant answer for your question.",
                "confidence": round(score, 2),
                "matched_question": None,
            }

        return {
            "answer": self.engine.answers[index],
            "confidence": round(score, 2),
            "matched_question": self.engine.questions[index],
        }
