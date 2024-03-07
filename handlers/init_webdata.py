from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

router = Router()

@router.message(content_types="web_app_data")
async def cmd_admin(message: Message, webAppMes):
    print(webAppMes) #вся информация о сообщении
    print(webAppMes.web_app_data.data) #конкретно то что мы передали в бота
    await message.answer(webAppMes.chat.id, f"получили инофрмацию из веб-приложения: {webAppMes.web_app_data.data}") 
    #отправляем сообщение в ответ на отправку данных из веб-приложения 
