from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

LANGUAGES = {
    "English": "en", "Spanish": "es", "French": "fr", "German": "de",
    "Hindi": "hi", "Telugu": "te", "Tamil": "ta", "Kannada": "kn",
    "Malayalam": "ml", "Japanese": "ja"
}

@app.route("/")
def index():
    return render_template("index.html", languages=LANGUAGES)

@app.post("/translate")
def translate():
    data = request.get_json(silent=True) or {}
    text = (data.get("text") or "").strip()
    source = data.get("source", "en")
    target = data.get("target", "te")

    if not text:
        return jsonify({"error": "Please enter text to translate."}), 400
    if source == target:
        return jsonify({"translatedText": text})

    # MyMemory is used as a no-key demo translation service.
    # Replace this endpoint with Google Cloud Translation or Microsoft Translator
    # credentials if your internship requires a paid/provider-specific API.
    try:
        r = requests.get(
            "https://api.mymemory.translated.net/get",
            params={"q": text, "langpair": f"{source}|{target}"},
            timeout=15
        )
        r.raise_for_status()
        data = r.json()
        translated = data.get("responseData", {}).get("translatedText")
        if not translated:
            return jsonify({"error": "Translation service returned no result."}), 502
        return jsonify({"translatedText": translated})
    except requests.RequestException as exc:
        return jsonify({"error": f"Translation service error: {exc}"}), 502

if __name__ == "__main__":
    app.run(debug=True)
