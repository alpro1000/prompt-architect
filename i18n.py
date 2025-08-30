import json
from pathlib import Path

_LOCALE_DIR = Path(__file__).parent / "locales"
_LANGUAGES = {
    "en": json.load((_LOCALE_DIR / "en.json").open(encoding="utf-8")),
    "ru": json.load((_LOCALE_DIR / "ru.json").open(encoding="utf-8")),
}

def detect_language(text: str) -> str:
    cyrillic_ratio = sum(1 for c in text if "а" <= c.lower() <= "я") / (len(text) + 1e-6)
    return "ru" if cyrillic_ratio > 0.3 else "en"

def t(key: str, lang: str) -> str:
    return _LANGUAGES.get(lang, _LANGUAGES["en"]).get(key, key)
