from aiogram import types
from random import randint
from aiogram.dispatcher.filters import Command

from loader import dp

@dp.message_handler(Command("meme"))
async def meme_cmd (message: types.Message):
    meme_url=["https://sun9-50.userapi.com/impg/VGf4E47mIZtau7L6zUDxMjc9n2ZMTcG1QVuwqQ/rxqwK1PAX5I.jpg?size=604x604&quality=96&sign=264bf5d9449e9f69ea4e1d350fa75781&type=album",
            "https://sun9-33.userapi.com/s/v1/ig2/gpnuA-FoMRYLbAEl4wiI3zAsrD2amq1X_J3PK6TgWG-vd4RaSttf4FrfnRM70znYnhqzi_p_fVy2XKveaN6upFZC.jpg?quality=95&as=32x18,48x27,72x40,108x61,160x90,240x135,360x202,480x270,540x304,640x360,720x405,1080x607,1280x720&from=bu&u=8gkwZNgwxc8SRRJe2IwNBL4YW67ESfkcyEOks9KWUmo&cs=807x454",
            "https://i.ytimg.com/vi/us0BF6Lv-4c/maxresdefault.jpg",
            "https://sun9-8.userapi.com/impg/4YcFYkgLuGnBUNbhC7eAGt1hdK2bwy3KxmGySg/6UXZtLxh4uo.jpg?size=828x664&quality=95&sign=fc020e5b291c39965c6c4d0ea3a9315e&c_uniq_tag=9y5VrxT3b15VY6H3rGpRb0SFiJLelTIIaDVqDaxeA5g&type=album",
            "https://avatars.mds.yandex.net/i?id=636f325a31a75d3af2a79e68454c991f56f106ee-12652282-images-thumbs&n=13",
            "https://sun9-36.userapi.com/impg/kmvTu7ndE20YAyX-4Mi24g1HmeKXBhW8W6-tjA/t07B96RzaNQ.jpg?size=1242x1492&quality=95&sign=d9455d20a79c72abd95ddf35d9c4dba4&c_uniq_tag=vaxqm1qgFDX6QxEMQ6ryzoqQj25_ibT_9KYI0f7UURI&type=album",
            "https://i.ytimg.com/vi/EyacUTt4bPs/maxresdefault.jpg",
            "https://avatars.mds.yandex.net/i?id=f466df04ebe00c4e7eb48c417c9412f3_l-4578697-images-thumbs&n=13"
              ]
    await message.answer_photo (
        photo=meme_url[randint(0, len(meme_url))]
    )