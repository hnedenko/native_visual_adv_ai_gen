from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import httpx

async def start_command(update: Update, context):
    await update.message.reply_text(
        "Hey! Send me any message and I`ll send you a new ad in response. This process could be endless!..)")

async def any_command(update: Update, context):
    user_input = update.message.text
    await update.message.reply_text(
        "It`s your new ad")

def main():
    from dotenv import load_dotenv
    import os
    load_dotenv(dotenv_path='.venv/.env')
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

    application = Application.builder().token(bot_token).build()

    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, any_command))

    # Запуск бота (он будет работать постоянно, ожидая сообщений)
    application.run_polling(poll_interval=1.0)

if __name__ == '__main__':
    main()