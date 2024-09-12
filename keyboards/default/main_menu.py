from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.dispatcher.filters import Text
from aiogram import types
from handlers.users.meme import meme_cmd

from loader import dp

menu=ReplyKeyboardMarkup(
    row_width=3,
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton("Обо мне")
        ],
        [
            KeyboardButton("Мем дня")
        ]

    ]
)

@dp.message_handler(Text(equals="Обо мне"))
async def show_about_me (message: types.Message):
    await message.answer("О вас: \n"
                         f"Ваше имя: {message.from_user.full_name}\n"
                         f"Ваше имя пользователя: {message.from_user.username}")

@dp.message_handler(Text(equals="Мем дня"))
async def show_meme_of_the_day (message: types.Message):
    await meme_cmd(message)
