import os
import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes

# Set up logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    filename="logfile.log"
)
logger = logging.getLogger(__name__)

# Get the token from environment variable
telegram_token = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.info(f"{update.message.date}: {update.message.from_user.id} - {update.message.text}")
    await update.message.reply_text("Esse chatbot está desativado!\nUse o novo chatbot @Dika_chatbot!")

def main() -> None:
    application = Application.builder().token(telegram_token).build()
    application.add_handler(MessageHandler(None, start))
    logger.info("Starting bot...")
    application.run_polling()

if __name__ == "__main__":
    main()
