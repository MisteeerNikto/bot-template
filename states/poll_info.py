from aiogram.dispatcher.filters.state import StatesGroup, State


class PollInfo(StatesGroup):
    q_1 = State()
    q_2 = State()
    q_3 = State()