from aiogram.loggers import webhook
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

home_button = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Get Location", request_location=True),
        KeyboardButton(text="Get Contact", request_contact=True)
    ],
    [
        KeyboardButton(text="Open web app", web_app=WebAppInfo(url="https://bekmurod-dev.netlify.app/"))
    ]
], resize_keyboard=True
)