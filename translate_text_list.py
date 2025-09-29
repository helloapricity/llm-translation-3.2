"""
translate_text_list.py
Translate a list of texts using OpenAI Chat Completions API.
Assignment 3.2: input is a list of strings + dest_language, return list of translated strings.
"""

from openai import OpenAI
import os
from typing import List, Optional
from dotenv import load_dotenv

# Load .env for API key
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Mapping codes -> language names
LANG_MAP = {
    "vi": "Vietnamese",
    "en": "English",
    "fr": "French",
    "es": "Spanish",
    "de": "German",
}

def _language_name(code_or_name: str) -> str:
    code_or_name = code_or_name.strip()
    if len(code_or_name) <= 3 and code_or_name.lower() in LANG_MAP:
        return LANG_MAP[code_or_name.lower()]
    return code_or_name

def translate_text(text: str, dest_language: str, client: Optional[OpenAI]=None) -> str:
    if client is None:
        client = globals().get("client")

    lang_name = _language_name(dest_language)
    prompt = f"Translate the following text into {lang_name}.\n\nText: \"{text}\"\n\nRespond ONLY with the translated text."
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a concise, professional translator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.0,
    )
    return resp.choices[0].message.content.strip()

def translate_text_list(text_list: List[str], dest_language: str, client: Optional[OpenAI]=None) -> List[str]:
    """
    Translate a list of texts into the destination language.
    Returns a list of translated strings.
    """
    translations = []
    for text in text_list:
        translated = translate_text(text, dest_language, client)
        translations.append(translated)
    return translations

if __name__ == "__main__":
    demo = {
        "text": ["Hello", "I am Peter"],
        "dest_language": "vi"
    }
    output = translate_text_list(demo["text"], demo["dest_language"])
    print(output)  # Expected: ["Xin chào", "Tôi tên là Peter"]