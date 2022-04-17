from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from django_bot.schedules.enums import DaysOfWeek


def get_button_schedule_keyboard():
    return InlineKeyboardMarkup(
        inline_keyboard=[[
                InlineKeyboardButton(
                    "Посмотреть рассписание",
                    callback_data='show_schedules'
                )
            ]
        ]
    )


def get_all_buttons_schedules():
    """Получить кнопки с рассписанием."""
    days_of_week = DaysOfWeek.choices
    list_buttons = []

    list_buttons.append(
        InlineKeyboardButton(
            "Сегодня",
            callback_data=f'day_of_week::today',
        )
    )

    for choice_day in days_of_week:
        list_buttons.append(
            InlineKeyboardButton(
                choice_day[1],
                callback_data=f'day_of_week::{choice_day[0]}',
            )
        )

    return InlineKeyboardMarkup([[button] for button in list_buttons])
