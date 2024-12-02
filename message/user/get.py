from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

async def get_answer(message: Message):
    if "/link" in message.text:
        number = message.text[6:]
        button = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Open", url=f"https://t.me/+{number}")
            ]
        ])
        return message.answer(f"Your link is here!", reply_markup=button)