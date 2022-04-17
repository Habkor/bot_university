from django_bot.faculties.models import Faculty
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_all_faculties():
    """Получить клавиатуру с факультетами."""

    faculties = Faculty.objects.all()

    list_buttons = []
    row_buttons = []

    for faculty in faculties:
        row_buttons.append(
            InlineKeyboardButton(
                faculty.name,
                callback_data=f'faculty::{faculty.name}',
            )
        )

        if len(row_buttons) == 3:
            list_buttons.append(row_buttons)
            row_buttons = []

    list_buttons.append(row_buttons)

    return InlineKeyboardMarkup(inline_keyboard=list_buttons)
