from telegram import Update
from telegram.ext import ContextTypes
from services.ai_chat import AIChat

async def chat_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    response = AIChat.get_response(user_text)
    await update.message.reply_text(response)
