from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_start_keyboard():
    """Функция возвращает стартовую клавиаутуру."""

    list_buttons = [
        InlineKeyboardButton("Декан", callback_data='decan'),
        InlineKeyboardButton("Преподаватель", callback_data='teacher'),
        InlineKeyboardButton("Студент", callback_data='student')
    ]

    return InlineKeyboardMarkup(inline_keyboard=[list_buttons])
