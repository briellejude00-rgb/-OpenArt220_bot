from telegram import Update
from telegram.ext import ContextTypes

async def help_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "💡 **OpenArt22_bot Guide**\n\n"
        "**Image Creation Examples:**\n"
        "`/logo minimalist coffee cup emblem`\n"
        "`/art floating glowing cyberpunk city`\n"
        "`/anime warrior with katana cinematic lighting`\n"
        "`/image sharp photo of a luxury sports car`\n\n"
        "**Text Chat:**\n"
        "Simply send a message without commands to talk to the AI assistant!"
    )
    await update.message.reply_text(text, parse_mode="Markdown")
