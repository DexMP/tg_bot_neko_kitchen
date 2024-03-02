import asyncio
import logging
from datetime import datetime
from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.filters.command import Command
from config_reader import config
from handlers import db_connect as db
from handlers import questions, admins

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()
dp.include_routers(questions.router, admins.router)
dp["started_at"] = datetime.now().strftime("%H:%M %d.%m.%Y")

async def on_startup():
    await db.db_start()
    await print('БД пашет')

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, on_startup=on_startup)

if __name__ == "__main__":
    asyncio.run(main())