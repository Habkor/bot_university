from telegram import InlineKeyboardMarkup
from telegram import InlineKeyboardButton


def suggestion_entry_password(chat_id):
    """Возвращает инлайн клавиатур для ввода пароля."""

    keyboard = [[InlineKeyboardButton("Ввести пароль декана", callback_data=f'entry_password::{chat_id}')]]

    return InlineKeyboardMarkup(keyboard)
