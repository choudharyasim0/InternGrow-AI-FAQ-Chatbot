import json
from pathlib import Path
from typing import Any

from flask import Flask, Response, jsonify, render_template, request

from chatbot import AIChatbot
from config import Config
from services.history_service import HistoryService


app = Flask(__name__)
app.config.from_object(Config)

bot = AIChatbot()
history_service = HistoryService()


def load_faq_questions() -> list[str]:
    dataset_path = Path("faq_dataset.json")
    with dataset_path.open(encoding="utf-8") as file:
        data = json.load(file)

    return [
        item["question"]
        for item in data
        if isinstance(item, dict) and isinstance(item.get("question"), str)
    ]


@app.route("/")
def home() -> str:
    return render_template("index.html", faq_questions=load_faq_questions())


@app.route("/chat", methods=["POST"])
def chat() -> Response:
    data: Any = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"answer": "Please enter a question."})

    message = data.get("message")
    if message is None:
        message = data.get("question", "")

    question = message.strip() if isinstance(message, str) else ""

    if not question:
        return jsonify({"answer": "Please enter a question."})

    result = bot.get_response(question)
    history_service.save(question, result["answer"])
    return jsonify(result)


@app.route("/history")
def history() -> Response:
    return jsonify(history_service.load())


@app.route("/clear", methods=["POST"])
def clear() -> Response:
    history_service.clear()
    return jsonify({"message": "History Cleared"})


if __name__ == "__main__":
    app.run(debug=True)
