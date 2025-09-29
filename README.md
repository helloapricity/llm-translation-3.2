# LLM Translation – Assignment 3.2

## Overview
This Python script translates a **list of texts** into a target language using the OpenAI Chat Completions API.
It extends Assignment 3.1 to handle multiple strings at once.

- Accepts language codes (e.g., "vi") or full language names ("Vietnamese").
- Returns a list of translated texts only.
- Deterministic output (`temperature=0`).

## Setup
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create `.env` in project root:
```bash
OPENAI_API_KEY=sk-xxxxxxx
```

3. Run the script:
```bash
python translate_text_list.py
```

Expected output:
```python
["Xin chào", "Tôi tên là Peter"]
```

4. Repository
Full code, tests, and instructions:
https://github.com/helloapricity/llm-translation-3.1

5. Tests
Run unit tests:
```bash
pytest -q
```