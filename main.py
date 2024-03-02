import asyncio
import logging
from datetime import datetime
from aiogram import Bot, Dispatcher, types
from aiogram import F
from aiogram.filters.command import Command
from config_reader import config

from handlers import questions, admins

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()
dp.include_routers(questions.router, admins.router)
dp["started_at"] = datetime.now().strftime("%H:%M %d.%m.%Y")
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, admins_list = [676094295, 658079279])

if __name__ == "__main__":
    asyncio.run(main())