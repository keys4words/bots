from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from config import API_KEY

# simple echo bot on base python-telegram-bot lib
def echo(update, context):
    update.message.reply_text(update.message.text)

updater = Updater(API_KEY, use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(Filters.text, echo))

updater.start_polling()

