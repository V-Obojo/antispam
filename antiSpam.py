from telegram import Update
from telegram.ext import CallbackContext
import logging

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def antispam_check(update: Update, context: CallbackContext):
    # Get message details
    message_text = update.message.text
    source = context.bot.username  # bot tag

        # Check for URLs in the message
    if 'http' in message_text or 'www' in message_text:
        try:
            # Delete the message with spam links
            context.bot.delete_message(chat_id=update.message.chat_id,
                                       message_id=update.message.message_id)
            print("Spam link deleted")
        except Exception as e:
            print(f"Error: {e}")
    else:
            pass
