# CodeAlpha Task 2 — Chatbot for FAQs

## AI/NLP approach
1. FAQ questions are loaded from `faqs.json`.
2. Text is cleaned using lowercase conversion and punctuation removal.
3. TF-IDF converts FAQ questions and the user's question into vectors.
4. Cosine similarity finds the closest FAQ.
5. A confidence threshold provides a fallback for unrelated questions.
6. Flask serves a simple chat interface.

## Run
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Open `http://127.0.0.1:5000`.
