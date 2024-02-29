from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

start_kb = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Бронь столика"),
            KeyboardButton(text="Заказ на дом")
        ],
        [
            KeyboardButton(text="Работа у нас"),
            KeyboardButton(text="Поддержка")
        ]
    ],
        resize_keyboard=True,
        input_field_placeholder="Выберите"
)

start_kb_admins = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Бронь столика"),
            KeyboardButton(text="Заказ на дом")

        ],
        [
            KeyboardButton(text="Работа у нас"),
            KeyboardButton(text="Админ-панель")
        ]
    ],
        resize_keyboard=True,
        input_field_placeholder="Выберите"
)

admin_panel = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Создать рассылку"),
            KeyboardButton(text="Отчёты")
        ],
        [
            KeyboardButton(text="ROOT") # будет удалении и добавление администраторов
        ],
        [
            KeyboardButton(text="Назад")
        ]
    ],
        resize_keyboard=True,
        input_field_placeholder="Выберите"
)