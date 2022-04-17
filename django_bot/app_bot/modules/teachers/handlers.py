from telegram.ext import ConversationHandler, CallbackQueryHandler, MessageHandler, Filters, CommandHandler

from django_bot.teachers.models import Teacher
from django_bot.core.bot import dispatcher
from django_bot.app_bot.modules.common.handlers import start


ENTRY_DIALOG_PASSWORD, ENTRY_END_DIALOG_TEACHER = range(2)


def register_teacher(update, _):
    """Регистрация учителя."""
    update.effective_message.reply_text(
        text="Здравствуйте, необходим ваш пароль",
    )

    return ENTRY_DIALOG_PASSWORD


def check_password_teacher(update, _):
    teacher = Teacher.objects.filter(
        password=update.message.text
    ).first()

    if teacher:
        # Устанавилваем decan.chat_id чтобы в случае чего использовать chat_ud
        if not teacher.chat_id:
            teacher.chat_id = update.effective_message.chat.id
            teacher.save(update_fields=['chat_id', ])

        update.effective_message.reply_text(
            text=f'{teacher.name} {teacher.patronymic}, добро пожаловать!',
        )
    else:
        update.effective_message.reply_text(
            text='Нажми заново /start'
        )

    return ConversationHandler.END


dispatcher.add_handler(
    ConversationHandler(
        entry_points=[
            CallbackQueryHandler(register_teacher, pattern='teacher')
        ],
        states={
            ENTRY_DIALOG_PASSWORD: [
                MessageHandler(filters=Filters.text, callback=check_password_teacher)
            ],
        },
        fallbacks=[CommandHandler('start', start)]
    )
)