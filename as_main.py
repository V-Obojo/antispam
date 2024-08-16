import nest_asyncio
nest_asyncio.apply()

from telegram.ext import Application, MessageHandler, filters
from antiSpam import antispam_check
import configparser
from pathlib import Path
import asyncio

# Bot token import
config = configparser.ConfigParser()
config_path = Path(__file__).parent / 'config.ini'
config.read(config_path)
token = config['TOKEN']['token']

async def main():
    # Create the Application and pass the bot token.
    application = Application.builder().token(token).build()

    # Add a message handler to handle all text messages
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, antispam_check))

    # Run the bot
    await application.run_polling()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
