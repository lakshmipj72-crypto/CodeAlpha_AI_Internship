from flask import Flask, render_template, request, jsonify
from faq_engine import FAQEngine

app = Flask(__name__)
engine = FAQEngine("faqs.json")

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/ask")
def ask():
    data = request.get_json(silent=True) or {}
    question = (data.get("question") or "").strip()
    if not question:
        return jsonify({"error": "Please enter a question."}), 400
    return jsonify(engine.answer(question))

if __name__ == "__main__":
    app.run(debug=True)
