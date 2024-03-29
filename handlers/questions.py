from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.main_menu import get_main_menu

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Выберите интересующий для вас раздел",
        reply_markup=get_main_menu()
    )
