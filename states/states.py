from aiogram.fsm.state import StatesGroup, State
class product_state(StatesGroup):
    name=State()
    price=State()