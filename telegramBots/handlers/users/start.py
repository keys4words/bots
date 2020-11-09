from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters.private_chat import IsPrivate
from loader import dp
from re import compile



@dp.message_handler(CommandStart(deep_link=compile(r"\d\d\d")), IsPrivate())
async def bot_start_deeplink(message: types.Message):
    deep_link_args = message.get_args()
    await message.answer(f'Hey, {message.from_user.full_name}!\n'
                        f'You are in personal correspondence.\n'
                        f'In you command is deep-link\n'
                        f'You send {deep_link_args}.\n')


@dp.message_handler(CommandStart(), IsPrivate())
async def bot_start(message: types.Message):
    bot_user = await dp.bot.get_me()
    deep_link = f"http://t.me/{bot_user.username}?start=123"
    await message.answer(f'Hey, {message.from_user.full_name}!\n'
                        f'You are in personal correspondence.\n'
                        f'In you command there is NO deep-link\n'
                        f'Your deep-link - {deep_link}')
                    