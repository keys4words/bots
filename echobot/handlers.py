from glob import glob
import logging

from telegram import Bot, Update

from echo.utils import *


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

def do_start(bot: Bot, update: Update, user_data):
    smile = get_user_emoji(user_data)
    user_data['smile'] = smile
    text = 'Hey! {}'.format(smile)
    update.message.reply_text(text, reply_markup=get_keyboard())
    logging.info('Bot started!')

def show_random_product(bot: Bot, update: Update, user_data):
    products_list = glob('images/p*.jpg')
    random_product = choice(products_list)
    bot.send_photo(chat_id=update.message.chat_id, photo=open(random_product, 'rb'), reply_markup=get_keyboard())

def show_random_cats(bot: Bot, update: Update, user_data):
    products_list = glob('images/cat*.jpg')
    random_product = choice(products_list)
    bot.send_photo(chat_id=update.message.chat_id, photo=open(random_product, 'rb'), reply_markup=get_keyboard())

def change_avatar(bot, update, user_data):
    if 'smile' in user_data:
        del user_data['smile']
    smile = get_user_emoji(user_data)
    update.message.reply_text('Avatar has changed: {}'.format(smile), reply_markup=get_keyboard())

def get_contact(bot, update, user_data):
    text = update.message.contact
    update.message.reply_text('Your contacts, {} {}: {}'.format(text.first_name, text.last_name, text.phone_number), reply_markup=get_keyboard())

def get_location(bot, update, user_data):
    text = update.message.location
    update.message.reply_text('Your location: {}'.format(text), reply_markup=get_keyboard())


def do_echo(bot: Bot, update: Update, user_data):
    smile = get_user_emoji(user_data)
    u_m = update.message.chat
    chat_id = u_m.id
    full_name = u_m.first_name + ' ' + u_m.last_name
    text = "{} написал\n'{}\n{}'".format(full_name, update.message.text, smile)
    update.message.reply_text(emojize(choice(config.EMOJI_LIST), use_aliases=True, reply_markup=get_keyboard()))
    logging.info("User: %s, Chat id: %s, Message: %s",
                 full_name, chat_id, update.message.text)

