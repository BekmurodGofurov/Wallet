from aiogram import Bot, Dispatcher
from asyncio import run
import config, message, keybords
from aiogram.fsm.storage.memory import MemoryStorage
from config import data as db
from config.command import set_bot_commands

async def start():
    bot = Bot(config.config.BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_routers(config.config_router, message.message_router)

    await db.db_start()
    print("Created SQLite")

    await set_bot_commands(bot)

    await dp.start_polling(bot, polling_timeout=1)

run(start())
