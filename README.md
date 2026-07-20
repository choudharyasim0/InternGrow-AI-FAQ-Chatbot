# 🤖 AI Context-Aware FAQ Chatbot

An AI-powered FAQ chatbot built with **Python**, **Flask**, and **Natural Language Processing (NLP)**. The chatbot understands user questions, finds the most relevant FAQ using **TF-IDF Vectorization** and **Cosine Similarity**, and provides intelligent responses through a clean, responsive web interface.

---

## 📌 Features

- AI-powered FAQ matching
- Natural Language Processing (NLP)
- TF-IDF Vectorizer
- Cosine Similarity search
- Conversation history
- Dark / Light mode
- Suggested questions
- Typing animation
- Responsive UI
- Clean and modern design

---

## 🛠️ Technologies Used

- Python 3
- Flask
- HTML5
- CSS3
- JavaScript
- Scikit-learn
- NLTK

---

## 📂 Project Structure

```
Task-02-AI-FAQ-Chatbot
│
├── app.py
├── chatbot.py
├── preprocess.py
├── config.py
├── faq_dataset.json
├── requirements.txt
│
├── services/
│   ├── history_service.py
│   └── nlp_service.py
│
├── history/
│   └── chat_history.json
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Task-02-AI-FAQ-Chatbot.git
```

### Go to Project

```bash
cd Task-02-AI-FAQ-Chatbot
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Project

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

## 💬 Sample Questions

- What is Artificial Intelligence?
- Explain Machine Learning
- What is Flask?
- Explain NLP
- What is Python?
- What is Data Science?

---

## 🚀 Future Improvements

- Voice Input
- Voice Output
- OpenAI / Gemini Integration
- Multi-language Support
- User Authentication
- Database Storage
- Chat Export
- AI Learning from New FAQs

---

## 👨‍💻 Author

**M Asim Imtiaz**

BS Artificial Intelligence

AI / ML Developer

---

## 📄 License

This project was developed for educational and internship purposes.