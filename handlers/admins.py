from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.admin_menu import get_admin_menu

router = Router()
# 1).DexMP  2). Василиса
admins = [676094295, 658079279]

@router.message(Command("admin"))
async def cmd_admin(message: Message):
    if message.from_user.id in admins:
        await message.answer("Запущена панель администратора", reply_markup=get_admin_menu())
    else:
        await message.answer("У вас нет прав для данной команды")
