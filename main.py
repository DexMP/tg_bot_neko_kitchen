import asyncio
import logging
from datetime import datetime
from aiogram import Bot, Dispatcher
from config_reader import config
from handlers import questions, admins, upload_data
from aiogram.utils.web_app import safe_parse_webapp_init_data
from aiohttp.web_request import Request
from aiohttp.web_response import json_response

logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()
dp.include_routers(questions.router, admins.router, upload_data.router)
dp["started_at"] = datetime.now().strftime("%H:%M %d.%m.%Y")


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

async def check_data_handler(request: Request):
    bot: Bot = request.app["bot"]

    data = await request.post()  # application/x-www-form-urlencoded
    try:
        data = safe_parse_webapp_init_data(token=config.bot_token.get_secret_value(), init_data=data["_auth"])
    except ValueError:
        return json_response({"ok": False, "err": "Unauthorized"}, status=401)
    return json_response({"ok": True, "data": data.user.dict()})

if __name__ == "__main__":
    asyncio.run(main())