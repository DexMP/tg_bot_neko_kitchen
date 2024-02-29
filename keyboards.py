from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

start_kb = ReplyKeyboardMarkup(
    keyboard = [
        [
            #KeyboardButton(text="Бронь столика"),
            #KeyboardButton(text="Заказ на дом")
        ],
        [
            #KeyboardButton(text="Работа у нас"),
            #KeyboardButton(text="Поддержка")
        ]
    ],
        resize_keyboard=True,
        input_field_placeholder="Выберите"
)