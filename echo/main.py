from glob import glob
from random import choice
import logging

from telegram import Bot, Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from emoji import emojize
from echo.config import MY_TOKEN, BASE_URL, PROXY
import echo.config as config


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

def get_user_emoji(user_data):
    if 'smile' in user_data:
        return user_data['smile']
    else:
        user_data['smile'] = emojize(choice(config.EMOJI_LIST), use_aliases=True)
        return user_data['smile']

def do_start(bot: Bot, update: Update, user_data):
    smile = get_user_emoji(user_data)
    user_data['smile'] = smile
    text = 'Hey! {}'.format(smile)
    update.message.reply_text(text)
    # bot.send_message(
    #     chat_id=update.message.chat_id,
    #     text='Hey! Send me something',
    # )
    logging.info('Bot started!')


def show_random_product(bot: Bot, update: Update, user_data):
    products_list = glob('images/p*.jpg')
    random_product = choice(products_list)
    bot.send_photo(chat_id=update.message.chat_id, photo=open(random_product, 'rb'))

def do_echo(bot: Bot, update: Update, user_data):
    smile = get_user_emoji(user_data)
    u_m = update.message.chat
    chat_id = u_m.id
    full_name = u_m.first_name + ' ' + u_m.last_name
    text = "{} написал\n'{}\n{}'".format(full_name, update.message.text, smile)
    # bot.send_message(
    #     chat_id=chat_id,
    #     text=text,
    # )
    update.message.reply_text(emojize(choice(config.EMOJI_LIST), use_aliases=True))
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
    start_handler = CommandHandler("start", do_start, pass_user_data=True)
    show_product = CommandHandler('products', show_random_product, pass_user_data=True)
    message_handler = MessageHandler(Filters.text, do_echo, pass_user_data=True)

    u_d = updater.dispatcher
    u_d.add_handler(start_handler)
    u_d.add_handler(show_product)
    u_d.add_handler(message_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
