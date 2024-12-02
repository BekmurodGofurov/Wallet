from aiogram.types import Message

from keybords.defolt.home import home_button

async def replay_answer(message: Message):
    await message.answer(f'Reply tugamalar', reply_markup=home_button)