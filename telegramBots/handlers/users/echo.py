from aiogram import types
from loader import dp


@dp.message_handler()
async def bot_echo(message: types.Message):
    # get chat_id and text
    chat_id = message.from_user.id
    text = message.text

    # get object Bot - from Dispatcher
    # bot = dp.bot

    # get object Bot - from context
    # from aiogram import Bot
    # bot = Bot.get_current()
    
    # get object Bot - from module loader
    from loader import bot

    # send message to user
    await bot.send_message(chat_id=chat_id, text=text)
    
    # send message to user without chat_id
    # await message.answer(text=text)

    # send message to user with reply
    # await message.reply(text=text)
