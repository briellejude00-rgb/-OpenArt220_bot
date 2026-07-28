from telegram import Update
from telegram.ext import ContextTypes
from services.image_generator import ImageGenerator

async def anime_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = " ".join(context.args)
    if not prompt:
        await update.message.reply_text("⚠️ Usage: `/anime <description>`", parse_mode="Markdown")
        return

    msg = await update.message.reply_text("🎨 Drawing anime art...")
    try:
        url = ImageGenerator.generate(prompt, mode="anime")
        await update.message.reply_photo(photo=url, caption=f"🎌 **Anime Prompt:** {prompt}", parse_mode="Markdown")
        await msg.delete()
    except Exception as e:
        await msg.edit_text(f"❌ Error: {e}")
