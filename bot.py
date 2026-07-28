import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import TELEGRAM_BOT_TOKEN
from database.database import init_db

# Import Handlers
from handlers.start import start_handler
from handlers.help import help_handler
from handlers.image import image_handler
from handlers.logo import logo_handler
from handlers.art import art_handler
from handlers.anime import anime_handler
from handlers.chat import chat_handler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

def main():
    if not TELEGRAM_BOT_TOKEN:
        logging.error("CRITICAL: TELEGRAM_BOT_TOKEN is missing!")
        return

    # Initialize SQLite DB
    init_db()

    # Build Bot Application
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Register Command Handlers
    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CommandHandler("help", help_handler))
    app.add_handler(CommandHandler("image", image_handler))
    app.add_handler(CommandHandler("logo", logo_handler))
    app.add_handler(CommandHandler("art", art_handler))
    app.add_handler(CommandHandler("anime", anime_handler))

    # Text Chat Handler (For non-command text)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat_handler))

    logging.info("@OpenArt22_bot is live and running...")
    app.run_polling()

if __name__ == "__main__":
    main()
