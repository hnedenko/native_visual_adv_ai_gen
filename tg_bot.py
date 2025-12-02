from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import os
from config_manager import ConfigManager
from modules.news_fetcher import NewsFetcher

async def start_command(update: Update, context):
    await update.message.reply_text(
        "Hi! Write me a topic you're interested in news about!..)")

async def any_command(update: Update, context):

    user_input = update.message.text
    gnews = news_fetcher.fetch_random_topic_gnews(user_input)

    await update.message.reply_text(gnews)

def main():
    from dotenv import load_dotenv
    import os
    load_dotenv(dotenv_path='.venv/.env')
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

    application = Application.builder().token(bot_token).build()

    # add handlers
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, any_command))

    application.run_polling(poll_interval=1.0)

if __name__ == '__main__':
    os.system('pip install -r requirements.txt')
    config_manager = ConfigManager()
    news_fetcher = NewsFetcher()
    main()