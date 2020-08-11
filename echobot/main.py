from telegram import Bot, Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters, RegexHandler

from echo.config import MY_TOKEN, BASE_URL, PROXY
from echo.handlers import *

def main():
    bot = Bot(
        token=MY_TOKEN,
        base_url=BASE_URL
    )
    updater = Updater(
        bot=bot,
    )
    start_handler = CommandHandler("start", do_start, pass_user_data=True)
    # show_product = CommandHandler('products', show_random_product, pass_user_data=True)
    show_product = CommandHandler('cats', show_random_cats, pass_user_data=True)
    message_handler = MessageHandler(Filters.text, do_echo, pass_user_data=True)

    message_handler_contacts = MessageHandler(Filters.contact, get_contact, pass_user_data=True)
    message_handler_location = MessageHandler(Filters.location, get_location, pass_user_data=True)

    # regex_handler_random_product = RegexHandler('^(Random product)$', show_random_product, pass_user_data=True)
    regex_handler_random_cat = RegexHandler('^(Random cat)$', show_random_cats, pass_user_data=True)
    regex_handler_change_avatar = RegexHandler('^(Change avatar)$', change_avatar, pass_user_data=True)

    u_d = updater.dispatcher
    u_d.add_handler(start_handler)
    u_d.add_handler(show_product)
    u_d.add_handler(regex_handler_random_cat)
    u_d.add_handler(regex_handler_change_avatar)

    u_d.add_handler(message_handler_contacts)
    u_d.add_handler(message_handler_location)

    u_d.add_handler(message_handler)


    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
