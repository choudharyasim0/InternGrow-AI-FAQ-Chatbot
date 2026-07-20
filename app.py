from typing import Any

from flask import Flask, Response, jsonify, render_template, request

from chatbot import AIChatbot
from config import Config
from services.history_service import HistoryService

app = Flask(__name__)
app.config.from_object(Config)

bot = AIChatbot()
history_service = HistoryService()


@app.route("/")
def home() -> str:
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat() -> Response:
    data: Any = request.get_json(silent=True)
    message = data.get("message", "") if isinstance(data, dict) else ""
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
