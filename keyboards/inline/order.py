from aiogram import types
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.dispatcher.filters import Text


from loader import dp

menu_button=InlineKeyboardButton(text="Меню",callback_data="menu")
delivery_button=InlineKeyboardButton(text="Условия доставки",callback_data="delivery")
address_button=InlineKeyboardButton(text="Адреса ресторанов",callback_data="address")


menu = InlineKeyboardMarkup(
    row_width=3,
    inline_keyboard=[
        [menu_button,delivery_button],
        [address_button]
    ]
)

@dp.callback_query_handler(Text(equals="menu"))
async def show_menu(call:types.CallbackQuery):
    await call.message.answer("Меню:\n"
                              "Суп из комаров 5Gp\n"
                              "Отбивные от Тагили 4Gp\n"
                              "Жареные Глаза Зрячего 3Gp\n"
                              "Гнездо Глухаря 3Gp\n"
                              "Жареные Сбеу комар 10Gp\n"
                              "Мясо по французки 4Gp\n"
                              "Буябес от Шефа(Виктора Килловича) 10Gp\n"
                              "Жареная Птица по Штурмански 4Gp\n"
                              "Говядина по Решальски 4Gp\n"
                              "Жареная Кобанятина 6Gp\n"
                              "Оливье по Буяновски 3Gp\n"
                              "Сайра по Колонтайски 2Gp\n"
                              "Суп по Кнайтски 5Gp\n"
                              "Взорваная рыба 4Gp\n"
                              "Жаренная птица от сушефа(Бирдай) 5Gp\n"
                              "Кокосовая труба 5Gp\n"
                              "slikers 1Gp\n"
                              "Карамельные яблоки от Чернобыля 2Gp\n")
    await call.message.answer("Напитки: \n"
                              "Коктель Санитарский 2Gp\n"
                              "Пиво Осёлиная моча 1Gp\n"
                              "Вода 0.5Gp\n"
                              "Квас Норвинский Ядрёный 1Gp\n"
                              "TarCola 1Gp\n"
                              "RatCola 1Gp\n"
                              "Сок Великий 1Gp\n"
                              "Соки в орсантимент 1Gp\n"
                              "Банка энергетика Чистая Энергия,Горячий электрод 1Gp\n")


@dp.callback_query_handler(Text(equals="delivery"))
async def show_delivery(call:types.CallbackQuery):
    await call.message.answer("Условия доставки:\n"
                              "Ваш адрес\n"
                              "Минимальная сумма заказа 2Gp монет\n"
                              "Радиус доставки 5км от ресторана\n")


@dp.callback_query_handler(Text(equals="address"))
async def show_address(call: types.CallbackQuery):
    await call.message.answer("Адреса:\n"
                              "Улица ленина\n" 
                              "Артамонова 28 к1\n"
                              "Хассанская 22 к 2")


@dp.message_handler(Text(equals="Заказ"))
async def making_order(message:types.Message):
    await message.answer(text="Сбеу комаринная кухня",reply_markup=menu)