from aiogram.types import Message

async def help(message: Message):
    await message.answer(f"/start - Botni qayta ishga tushirish\n/add - Malumot qo'shish\n/data - Malumotni ko'rish\n/help - Yordam olish")