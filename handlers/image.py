from telegram import Update
from telegram.ext import ContextTypes
from services.image_generator import ImageGenerator

async def image_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = " ".join(context.args)
    if not prompt:
        await update.message.reply_text("⚠️ Usage: `/image <description>`", parse_mode="Markdown")
        return

    msg = await update.message.reply_text("📸 Generating realistic photo...")
    try:
        url = ImageGenerator.generate(prompt, mode="image")
        await update.message.reply_photo(photo=url, caption=f"✨ **Prompt:** {prompt}", parse_mode="Markdown")
        await msg.delete()
    except Exception as e:
        await msg.edit_text(f"❌ Error: {e}")
