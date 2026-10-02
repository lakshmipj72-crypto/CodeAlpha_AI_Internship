# CodeAlpha Task 1 — Language Translation Tool

## Features
- Text input
- Source and target language selection
- Translation API request
- Clear translated output
- Copy button
- Responsive UI

## Run
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

pip install -r requirements.txt
python app.py
```
Open `http://127.0.0.1:5000`.

### API note
This demo uses the no-key MyMemory translation endpoint so the project can run without exposing a paid API key. If CodeAlpha specifically requires Google Translate or Microsoft Translator, replace the request in `app.py` with that provider's authenticated API.
