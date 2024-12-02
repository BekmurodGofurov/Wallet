from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

product_list = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Food", callback_data="Food"),
        InlineKeyboardButton(text="Taxi", callback_data="Taxi")
    ],
    [
        InlineKeyboardButton(text="Other", callback_data='Other')
    ]
])