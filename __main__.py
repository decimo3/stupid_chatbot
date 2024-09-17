import sys
import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes

# Get the token from environment variable
telegram_token = sys.argv[1]
telegran_identify = telegram_token.split(':')[0]

# Set up logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    filename=f"{telegran_identify}.log"
)
logger = logging.getLogger(__name__)

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
