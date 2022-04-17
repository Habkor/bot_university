from telegram.ext import CallbackQueryHandler, ConversationHandler, CommandHandler
from django_bot.schedules.models import ScheduleForStudent
from datetime import datetime
from django_bot.app_bot.modules.schedules.helpers import is_numerator_week
from django_bot.app_bot.modules.common.handlers import start
from django_bot.app_bot.keyboards.schedules.schedules import get_all_buttons_schedules
from django_bot.core.bot import dispatcher

CHOOSE_WHEN_SCHEDULE = range(1)


def choose_days(update, _):
    """После нажатия на показать рассписание."""
    update.effective_message.reply_text(
        "В какой день вы хотите узнать рассписание",
        reply_markup=get_all_buttons_schedules()
    )

    return CHOOSE_WHEN_SCHEDULE


def choose_when_schedule(update, _):
    """Обработка нажатия на выбранный день."""
    numerator = is_numerator_week(datetime.now().date())
    schedule = ScheduleForStudent.objects.filter(
        order=numerator,
        days_of_week=update.callback_query.data.split('::')[1],
    ).first()

    if schedule:
        update.effective_message.reply_text(
            schedule.text_schedule
        )
    else:
        update.effective_message.reply_text(
            "Администратор не задал рассписание на этот день"
        )

    return ConversationHandler.END


dispatcher.add_handler(
    ConversationHandler(
        entry_points=[
            CallbackQueryHandler(choose_days, pattern='show_schedules')
        ],
        states={
            CHOOSE_WHEN_SCHEDULE: [
                CallbackQueryHandler(
                    choose_when_schedule,
                    pattern='day_of_week::[-\w]+'
                )
            ]
        },
        fallbacks=[CommandHandler('start', start)]
    )
)
