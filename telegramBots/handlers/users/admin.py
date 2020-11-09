from aiogram import types
from filters.private_chat import IsPrivate
from loader import dp

from data.config import admins



@dp.message_handler(IsPrivate(), text='secret', user_id=admins)
async def admin_chat_secret(message: types.Message):
    await message.answer('This is secret message from one admin in private correspondence')