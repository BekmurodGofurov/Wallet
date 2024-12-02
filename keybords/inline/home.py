from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Callback", callback_data="$data"),
     InlineKeyboardButton(text="URL", url="https://bekmurod-dev.netlify.app/"),
     InlineKeyboardButton(text="Search", switch_inline_query_current_chat=""),
     InlineKeyboardButton(text="Share", switch_inline_query="Tavsiya qilaman!")],
    [
        InlineKeyboardButton(text="web app", web_app=WebAppInfo(url="https://bekmurod-dev.netlify.app/"))
    ]
])