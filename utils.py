from telebot import types
from typing import List, Any

class State:
    group: str
    week_day: str

    def __init__(self):
        self.group = ""
        self.week_day = ""

    def reset(self):
        self.group = ""
        self.week_day = ""

def create_reply_keyboard(
    items: List[str],
    resize_keyboard: bool or None = None,
    one_time_keyboard: bool or None = None,
    input_field_placeholder: Any or None = None,
    selective: bool or None = None,
    row_width: int = 3,

) -> types.ReplyKeyboardMarkup:
    markup = types.ReplyKeyboardMarkup(
        resize_keyboard=resize_keyboard,
        one_time_keyboard=one_time_keyboard,
        input_field_placeholder=input_field_placeholder,
        selective=selective,
        row_width=row_width
    )

    for button_text in items:
        keyboard_button = types.KeyboardButton(button_text)
        markup.add(keyboard_button)

    return markup


valid_groups = ["УВП-111", "УВП-112", "УВВ-111", "УИС-111", "УИС-112"]
valid_days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]
