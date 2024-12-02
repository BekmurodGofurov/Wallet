from aiogram import Bot
from aiogram.types import Message
from config.config import ADMIN_ID
from config.data import get_user, new_user

async def welcome(message: Message, bot: Bot):
    user_id = message.from_user.id
    name = message.from_user.full_name
    username = f"@{message.from_user.username}"
    is_bot = message.from_user.is_bot
    age = 0
    auth="False"

    user = get_user(user_id)

    if is_bot != True:
        if user:
            await message.answer(f"Sizni botda qayta ko'rib turganimda judaham hursandman, {name}!")
        else:
            # Add user to database
            if new_user(user_id, name, username, age, auth):
                await message.answer(f"Assalomu alekum {name}!\nBizning botimizga hush kelibsiz.\n\n\n/help \t--\t Yordam olish")
                await bot.send_message(ADMIN_ID, f"{message.from_user.mention_html()} botga qo'shildi", parse_mode="HTML")
            else:
                    # Handle potential duplicate addition errors (if applicable)
                await message.answer("Qandeydur xatolik yuz berdi. Iltimos keyinroq qayta urinib ko'ring!")
    else:
        await message.answer("""||--YOU-ARE-A-BOT--||""")