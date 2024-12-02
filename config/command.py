from aiogram.types import BotCommand

async def set_bot_commands(bot):
    await bot.set_my_commands([
        BotCommand(command="/start", description="Botni qayta ishga turshirish!"),
        BotCommand(command="/add", description="Add data"),
        BotCommand(command="/data", description="Get the data"),
        BotCommand(command="/help", description="Yordam olish!")

    ])