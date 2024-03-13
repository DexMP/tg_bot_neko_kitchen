from aiogram import Router, F
from aiogram.types import WebAppInfo, WebAppData, SentWebAppMessage
from aiogram.types import Message
from aiogram import types

router = Router()

@router.inline_query()
async def cmd_start(message: Message):
    await message.answer("Выберите интересующий для вас раздел",)