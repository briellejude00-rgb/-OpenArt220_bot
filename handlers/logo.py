from telegram import Update
from telegram.ext import ContextTypes
from services.image_generator import ImageGenerator

async def logo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    prompt = " ".join(context.args)
    if not prompt:
        await update.message.reply_text("⚠️ Usage: `/logo <description>`", parse_mode="Markdown")
        return

    msg = await update.message.reply_text("✏️ Designing your logo...")
    try:
        url = ImageGenerator.generate(prompt, mode="logo")
        await update.message.reply_photo(photo=url, caption=f"🎨 **Logo Prompt:** {prompt}", parse_mode="Markdown")
        await msg.delete()
    except Exception as e:
        await msg.edit_text(f"❌ Error: {e}")
