from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv
import os
from config import BOT_TOKEN
from i18n import get_text
from generator import generate_reply

load_dotenv()

async def start(update, context):
    await update.message.reply_text(get_text('start'))

async def handle_message(update, context):
    user_input = update.message.text
    response = await generate_reply(user_input)
    await update.message.reply_text(response)

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

if __name__ == '__main__':
    print("✅ Бот запускается...")
    app.run_polling()
