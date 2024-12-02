from aiogram.types import Message, CallbackQuery
from config.data import add_data_wallet, get_wallet_data
from keybords.defolt.products import product_list
from states.states import product_state

from aiogram.fsm.context import FSMContext

async def add_start(message: Message, state: FSMContext):
    await message.answer('Quyda berilganlardan birini tanlang', reply_markup=product_list)
    await state.set_state(product_state.name)

async def add_price(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Sariflangan summani kiriting $")
    await state.set_state(product_state.price)

async def done(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    user_id = message.from_user.id
    data = await state.get_data()
    name = data.get("name")
    price = data.get('price')
    add_data_wallet(user_id, name, price)
    await message.answer("Sizning malumotingiz saqalandi. \n/data - Malomotlarni ko'rish")
    await state.clear()

async def send_data(message: Message):
    data = get_wallet_data(message.from_user.id)

    if data:
        anser = f"\bWallet\nProduct  \tPrice\t  Time\n"
        for i in data:
            anser += f"""
{i[1]}  \t{i[2]}$  \t{i[3]}    
____________________________________
"""
    else:
        anser+="Sizda malumot mavjud emas!"
    await message.answer(anser)



async def add_week(message: Message):
    user_id = message.text


