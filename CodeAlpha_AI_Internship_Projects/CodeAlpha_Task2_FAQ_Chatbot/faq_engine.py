import json
import re
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class FAQEngine:
    def __init__(self, faq_file):
        data = json.loads(Path(faq_file).read_text(encoding="utf-8"))
        self.faqs = data["faqs"]
        self.questions = [self.clean(x["question"]) for x in self.faqs]
        self.vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words="english")
        self.matrix = self.vectorizer.fit_transform(self.questions)

    @staticmethod
    def clean(text):
        text = text.lower()
        text = re.sub(r"[^a-z0-9\s]", " ", text)
        return re.sub(r"\s+", " ", text).strip()

    def answer(self, question):
        cleaned = self.clean(question)
        query_vector = self.vectorizer.transform([cleaned])
        scores = cosine_similarity(query_vector, self.matrix)[0]
        best_index = int(scores.argmax())
        score = float(scores[best_index])

        # Threshold prevents unrelated questions from receiving a misleading FAQ answer.
        if score < 0.15:
            return {
                "answer": "Sorry, I could not find a matching FAQ. Please try another question.",
                "confidence": round(score, 3),
                "matched_question": None
            }

        faq = self.faqs[best_index]
        return {
            "answer": faq["answer"],
            "confidence": round(score, 3),
            "matched_question": faq["question"]
        }
