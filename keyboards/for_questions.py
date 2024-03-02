from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_yes_no_kb() -> ReplyKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="Да", url="https://github.com")
    kb.button(text="Нет", url="https://github.com")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)