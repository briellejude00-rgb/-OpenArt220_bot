from telegram import Update
from telegram.ext import ContextTypes
from database.database import register_user

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    register_user(user.id, user.username or "", user.first_name or "")

    text = (
        f"🎨 **Welcome to @OpenArt22_bot, {user.first_name}!**\n\n"
        "I can generate multi-style AI images and chat with you!\n\n"
        "**Commands:**\n"
        "• `/image <prompt>` - Generate Realistic Image\n"
        "• `/logo <prompt>` - Generate Professional Logo\n"
        "• `/art <prompt>` - Generate Digital Art\n"
        "• `/anime <prompt>` - Generate Anime Art\n"
        "• `/help` - Show Help Guide\n\n"
        "💬 *Or just send me any text message to chat with AI!*"
    )
    await update.message.reply_text(text, parse_mode="Markdown")
