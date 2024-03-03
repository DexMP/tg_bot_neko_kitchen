import asyncio
import logging
from datetime import datetime
from aiogram import Bot, Dispatcher
from config_reader import config
from handlers import questions, admins, input_data

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()
dp.include_routers(questions.router, admins.router, input_data.router)
dp["started_at"] = datetime.now().strftime("%H:%M %d.%m.%Y")


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())