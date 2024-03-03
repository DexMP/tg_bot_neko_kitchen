from aiogram import Router
from aiogram.types import Message


router = Router()

@router.message()
async def web_app(message: Message):
    await message.answer(message.web_app_data.data)
