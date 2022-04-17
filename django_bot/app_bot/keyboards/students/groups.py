from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from django_bot.groups.models import Group


def get_groups_keyboard(faculty_name):
    """Функция возвращает клавиаутуру для декана."""
    groups = Group.objects.filter(
        faculty__name=faculty_name
    )

    list_buttons = []
    row_buttons = []

    for group in groups:
        row_buttons.append(
            InlineKeyboardButton(
                group.group_name,
                callback_data=f'group::{group.group_name}',
            )
        )

        if len(row_buttons) == 3:
            list_buttons.append(row_buttons)
            row_buttons = []

    list_buttons.append(row_buttons)

    return InlineKeyboardMarkup(inline_keyboard=list_buttons)
