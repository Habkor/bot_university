from django_bot.faculties.models import Faculty
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_all_faculties():
    """Получить клавиатуру с факультетами."""

    faculties = Faculty.objects.all()

    list_buttons = []

    for faculty in faculties:
        list_buttons.append(
            InlineKeyboardButton(
                faculty.name,
                callback_data=f'faculty::{faculty.name}',
            )
        )

    return InlineKeyboardMarkup(inline_keyboard=[list_buttons])
