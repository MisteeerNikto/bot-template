from aiogram import types


from loader import dp


@dp.message_handler(content_types=types.ContentTypes.ANY)
async def get_file_id(message:types.Message):
    if message.photo:
        photo_file_id=message.photo[0].file_id

        await message.reply(f"Файл id этой фотографии - <code>{photo_file_id}</code>")
    elif message.voice:
        voice_file_id=message.voice.file_id

        await message.reply(f"Файл id этого голосового сообщения - <code>{voice_file_id}</code>")

    elif message.sticker:
        sticker_file_id=message.sticker.file_id

        await message.reply(f"Файл id этого стикера - <code>{sticker_file_id}</code>")