from groups.models import Group
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup


def form_keyboard_with_groups():
    """Формирует клавиатуру с группами."""
    groups = Group.objects.all()

    buttons_list = []

    for group in groups:
        buttons_list.append(
            InlineKeyboardButton(
                group.group_name, callback_data=f'{group.group_name},'
            )
        )

    return InlineKeyboardMarkup(buttons_list)
