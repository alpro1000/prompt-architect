from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from prompts.generator import generate_prompt_yaml
from i18n import detect_language, t

BOT_TOKEN = "YOUR_TOKEN_HERE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = detect_language(update.effective_user.language_code or "")
    await update.message.reply_text(t("welcome", lang))

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    lang = detect_language(text)
    await update.message.reply_text(t("generating", lang))
    
    try:
        prompt = generate_prompt_yaml(text, lang=lang)
        await update.message.reply_text(f"📦 {t('output_title', lang)}\n\n```yaml\n{prompt}\n```", parse_mode="MarkdownV2")
    except Exception as e:
        await update.message.reply_text(t("error", lang))

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
app.run_polling()

