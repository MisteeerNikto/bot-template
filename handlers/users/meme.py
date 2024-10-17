from aiogram import types
from random import randint
from aiogram.dispatcher.filters import Command

from loader import dp

@dp.message_handler(Command("meme"))
async def meme_cmd (message: types.Message):
    meme_url=["https://sun9-50.userapi.com/impg/VGf4E47mIZtau7L6zUDxMjc9n2ZMTcG1QVuwqQ/rxqwK1PAX5I.jpg?size=604x604&quality=96&sign=264bf5d9449e9f69ea4e1d350fa75781&type=album",
            "https://sun9-33.userapi.com/s/v1/ig2/gpnuA-FoMRYLbAEl4wiI3zAsrD2amq1X_J3PK6TgWG-vd4RaSttf4FrfnRM70znYnhqzi_p_fVy2XKveaN6upFZC.jpg?quality=95&as=32x18,48x27,72x40,108x61,160x90,240x135,360x202,480x270,540x304,640x360,720x405,1080x607,1280x720&from=bu&u=8gkwZNgwxc8SRRJe2IwNBL4YW67ESfkcyEOks9KWUmo&cs=807x454",
            "https://i.ytimg.com/vi/us0BF6Lv-4c/maxresdefault.jpg"
              ]
    await message.answer_photo (
        photo=meme_url[randint(0, len(meme_url))]
    )