from aiogram.types import Message

from keybords.inline.home import inline_keyboard

async def home(message: Message):
    await message.answer(f"Inline tugmalar test uchun: ", reply_markup=inline_keyboard)