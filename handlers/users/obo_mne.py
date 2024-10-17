from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext


from loader import dp
from states.poll_info import PollInfo


@dp.message_handler(Command('poll'))
async def poll_cmd (messages: types.Message):
    await messages.answer("1.Дигл есть на 9.33?")

    await PollInfo.q_1.set()


@dp.message_handler(state=PollInfo.q_1)
async def get_first_answer(messages: types.Message, state: FSMContext):
    answer = messages.text

    await state.update_data(
        {
            'q_1' : answer
        }
    )

    await messages.answer("1.Таркову 8 лет?")
    await PollInfo.q_2.set()


@dp.message_handler(state=PollInfo.q_2)
async def get_second_answer(messages: types.Message, state: FSMContext):
    answer = messages.text

    await state.update_data(
        {
            'q_2' : answer
        }
    )

    data = await state.get_data()

    q_1 = data.get('q_1')
    q_2 = data.get('q_2')

    await messages.answer(f"Ваши ответы: {q_1},{q_2}\n"
                          
                         "Правильные ответы: 1.да 2.нет 3.нет")

    await state.reset_state()
