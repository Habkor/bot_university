from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_decan_keyboard(chat_id: str):
    """Функция возвращает клавиаутуру для декана."""
    list_buttons = [
        InlineKeyboardButton("Ввести сообщение для всех студентов", callback_data=f'send_message::{chat_id}'),
    ]

    return InlineKeyboardMarkup(inline_keyboard=[list_buttons])
