from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from echo.config import MY_TOKEN, BASE_URL, PROXY
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

def do_start(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text='Hey! Send me something',
    )
    logging.info('Bot started!')

def do_echo(bot: Bot, update: Update):
    u_m = update.message.chat
    chat_id = u_m.id
    full_name = u_m.first_name + ' ' + u_m.last_name
    text = "{} написал\n'{}'".format(full_name, update.message.text)
    bot.send_message(
        chat_id=chat_id,
        text=text,
    )
    logging.info("User: %s, Chat id: %s, Message: %s",
                 full_name, chat_id, update.message.text)


def main():
    bot = Bot(
        token=MY_TOKEN,
        base_url=BASE_URL
    )
    updater = Updater(
        bot=bot,
    )
    # updater = Updater(
    #     bot=bot,
    #     request_kwargs=PROXY
    # )
    start_handler = CommandHandler("start", do_start)
    message_handler = MessageHandler(Filters.text, do_echo)
    u_d = updater.dispatcher
    u_d.add_handler(start_handler)
    u_d.add_handler(message_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
