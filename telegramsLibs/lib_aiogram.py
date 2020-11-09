from aiogram import Bot, Dispatcher, executor, types
from config import API_KEY


bot = Bot(token=API_KEY)
dp = Dispatcher(bot)

@dp.message_handler()
async def get_message(message: types.Message):
    chat_id = message.chat.id
    #######################
    # write text in chat
    # text = 'Some text'
    # send_message = await bot.send_message(chat_id=chat_id, text=text)
    # print(send_message.to_python())

    #######################
    # send photo to chat
    # send_message = await bot.send_photo(chat_id=chat_id, photo="https://images.unsplash.com/photo-1574144611937-0df059b5ef3e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2000&q=80")
    # print(send_message.photo[-1].file_unique_id)

    #######################
    # change chat title
    # result = await bot.set_chat_title(chat_id=chat_id, title='Testing chat')
    # print(result)

    #######################
    # get private link from chat
    # invite_link = await bot.export_chat_invite_link(chat_id=chat_id)
    # print(invite_link)

    #######################
    # get bot's username
    bot_user = await bot.get_me()
    print(bot_user.username)

executor.start_polling(dp)