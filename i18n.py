from config import LANG

i18n_texts = {
    "start": {
        "ru": "Привет! Я Архитектор Промтов. Напиши мне что-нибудь...",
        "en": "Hello! I'm Prompt Architect. Send me something to get started."
    }
}

def get_text(key):
    return i18n_texts.get(key, {}).get(LANG, "[missing text]")
