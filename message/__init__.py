from aiogram import Router

from . import user
from . import channel
from . import admin

message_router = Router()

message_router.include_routers(user.user_router)