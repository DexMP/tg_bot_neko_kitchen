from aiogram.types import ReplyKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_admin_menu() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Изменить меню")
    kb.button(text="Отзывы")
    kb.button(text="Роли")
    kb.button(text="Отчёты")
    kb.button(text="Отзывы")
    kb.button(text="Начислить бонусы")
    kb.button(text="Создать рассылку")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)