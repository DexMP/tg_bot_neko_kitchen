from aiogram.types import ReplyKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_main_menu() -> ReplyKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="🍜  Меню", web_app=WebAppInfo(url="https://dexmp.ru"))
    kb.button(text="🍽 Бронирование стола", web_app=WebAppInfo(url="https://dexmp.ru"))
    kb.button(text="😊 Профиль", web_app=WebAppInfo(url="https://dexmp.ru"))
    kb.button(text="📋 Мои заказы", web_app=WebAppInfo(url="https://dexmp.ru"))
    kb.button(text="🎖 Отзывы", web_app=WebAppInfo(url="https://dexmp.ru"))
    kb.button(text="📍 Наши контакты", web_app=WebAppInfo(url="https://dexmp.ru"))
    kb.button(text="📍 Наши контакты", web_app=WebAppInfo(url="https://dexmp.ru"))
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True)

# DeepLink @this_burger_bot https://t.me/this_burger_bot?start=74078