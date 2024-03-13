from aiogram.types import ReplyKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

def get_main_menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="🍜  Меню", web_app=WebAppInfo(url="https://neko-kitchen.ru"))
    kb.button(text="🍽 Бронирование стола", web_app=WebAppInfo(url="https://neko-kitchen.ru"))
    kb.button(text="😊 Профиль", web_app=WebAppInfo(url="https://neko-kitchen.ru"))
    kb.button(text="📋 Мои заказы", web_app=WebAppInfo(url="https://neko-kitchen.ru"))
    kb.button(text="🎖 Отзывы", web_app=WebAppInfo(url="https://neko-kitchen.ru"))
    kb.button(text="📍 Наши контакты", web_app=WebAppInfo(url="https://neko-kitchen.ru"))
    kb.button(text="🥺 Рефералка", switch_inline_query="https://t.me/Neko_kitchen_bot")
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)