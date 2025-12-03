from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import os
from modules.news_fetcher import NewsFetcher
from publishers.publishers import Publishers
from modules.native_ad_AI_gen import NativeAdAIGen
import random

async def start_command(update: Update, context):
    await update.message.reply_text(
        "Hi! Write me a topic you're interested in news about!..)")

async def any_command(update: Update, context):

    user_input = update.message.text

    # get 1 random gnews
    contextual_gnews = news_fetcher.fetch_random_topic_gnews(user_input)
    await update.message.reply_text('News:\n\n'+contextual_gnews)

    # get random publisher for advertising generation
    # TODO: implement vectorization publishers and news, choose not random, but weighted and/or nearest
    advertised_publisher = random.choice(Publishers().publishers)
    await update.message.reply_text('Publisher:\n\n'+advertised_publisher["name"])

    # advertising generation from gnews context and advertised publisher
    native_ad_AI_gen = NativeAdAIGen()
    response = native_ad_AI_gen.generate_ad(contextual_gnews, advertised_publisher["visual"])
    print(response)
    # TODO: implement image extracting from response

    # TODO: implement filters logic and AI-ComfyUI

    # TODO: implement regenerating image if one of filters more then threshold

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
    news_fetcher = NewsFetcher()
    main()