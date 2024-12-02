from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

product_list = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Food",),
        KeyboardButton(text="Taxi",)
    ],
    [
        KeyboardButton(text="Other",)
    ]
], resize_keyboard=True,
one_time_keyboard=True)