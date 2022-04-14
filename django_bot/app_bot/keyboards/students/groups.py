from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from django_bot.groups.models import Group


def get_groups_keyboard():
    """Функция возвращает клавиаутуру для декана."""
    groups = Group.objects.all()

    list_buttons = []

    for group in groups:
        list_buttons.append(
            InlineKeyboardButton(
                group.group_name,
                callback_data=f'group::{group.group_name}',
            )
        )

    return InlineKeyboardMarkup(inline_keyboard=[list_buttons])