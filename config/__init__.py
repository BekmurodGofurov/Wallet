from aiogram import Router, F

from . import config
from . import navigation
from .command import set_bot_commands

config_router = Router()

config_router.startup.register(navigation.startup_answer)
config_router.shutdown.register(navigation.shutdown_answer)
