from aiogram import Bot
from config.config import ADMIN_ID

async def startup_answer(bot: Bot):
    await bot.send_message(ADMIN_ID, f"Bot ishga tushdi 😊")

async def shutdown_answer(bot: Bot):
    await bot.send_message(ADMIN_ID, "Bot ishdan to'xtadi ❌")
