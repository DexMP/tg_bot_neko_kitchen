import asyncio
import logging
import keyboards
from datetime import datetime
from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.filters.command import Command
from config_reader import config

# 1).DexMP  2). Василиса

admins = [676094295, 658079279]

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()
dp["started_at"] = datetime.now().strftime("%H:%M %d.%m.%Y")

# Проверка запуска бота
@dp.message(Command("info"))
async def cmd_info(message: types.Message, started_at: str):
    await message.answer(f"Бот запущен {started_at}")

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    if message.from_user.id in admins:
        await message.answer("Меню добавлено снизу", reply_markup=keyboards.main_kb_admins)
    else:
        await message.answer("Меню добавлено снизу", reply_markup=keyboards.main_kb)

@dp.message(F.text.lower() == "назад")
async def today(message: types.Message):
    await message.answer("Меню добавлено снизу", reply_markup=keyboards.main_kb_admins)
    
@dp.message(F.text.lower() == "🚗 сегодня")
async def today(message: types.Message):
    await message.answer("Машины на сегодня")

@dp.message(F.text.lower() == "🚗 завтра")
async def yesturday(message: types.Message):
    await message.answer("Машины на завтра")

@dp.message(F.text.lower() == "админ-панель")
async def yesturday(message: types.Message):
    if message.from_user.id in admins:
        await message.answer("Вы вошли как администратор", reply_markup=keyboards.admin_panel)
    else:
        await message.answer("")

@dp.message(Command("rearm"))
async def cmd_rearm(message: types.Message):
    await message.answer("Сканирование таблицы запущено")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())