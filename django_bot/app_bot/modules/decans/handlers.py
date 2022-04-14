from django_bot.app_bot.keyboards.decans.send_message import get_decan_keyboard
from django_bot.core.bot import dispatcher
from django_bot.decans.bot.keyboard import suggestion_entry_password
from django_bot.decans.models import Decan
from django_bot.students.models import Student
from telegram.ext import ConversationHandler
from telegram.ext import CallbackQueryHandler, Filters, MessageHandler, CommandHandler
from django_bot.app_bot.modules.common.handlers import start
from django_bot.core.helpers import send_async_message


ENTRY_PASSWORD_DECAN, COMPARE_PASSWORD_DECAN = range(2)
ENTRY_MESSAGE_DECAN = range(1)


def entry_point_decan(update, _):
    update.effective_message.reply_text(
        text="Здравствуйте, необходим ваш пароль",
        reply_markup=suggestion_entry_password(update.callback_query.from_user.id)
    )

    return ENTRY_PASSWORD_DECAN


def handler_password(update, context):
    """Эта функция срабатывается после нажатия деканаом кнопки отправить пароль."""
    update.effective_message.reply_text(
        text='Введите ваш пароль',
    )

    return COMPARE_PASSWORD_DECAN


def handler_compare_password(update, context):
    """Сравнивает пароль заданный через админку."""
    decan = Decan.objects.filter(
        password=update.message.text
    ).first()

    if decan:

        # Устанавилваем decan.chat_id чтобы в случае чего использовать chat_ud
        if not decan.chat_id:
            decan.chat_id = update.effective_message.chat.id
            decan.save(update_fields=['chat_id', ])

        update.effective_message.reply_text(
            text=f'{decan.name} {decan.patronymic}, добро пожаловать!',
            reply_markup=get_decan_keyboard(update.effective_message.chat.id)
        )

    else:
        update.effective_message.reply_text(
            text='Нажми заново /start'
        )

    return ConversationHandler.END


def handler_write_message(update, context):
    """"Ввод того сообщения, которого необходимо отправить."""
    update.effective_message.reply_text(
        text='Введите ваше сообщение для студентов',
    )

    return ENTRY_MESSAGE_DECAN


def handler_send_message_students(update, context):
    """Отправка сообщений для всех студентов"""
    decan = Decan.objects.filter(
        chat_id=update.effective_message.chat.id
    ).first()

    name_faculty = decan.faculty
    students = Student.objects.filter(
        group__faculty=name_faculty
    )

    for student in students:
        send_async_message(
            context,
            update.message.text,
            student.chat_id,
        )

    return ConversationHandler.END


dispatcher.add_handler(
    ConversationHandler(
        entry_points=[
            CallbackQueryHandler(entry_point_decan, pattern='decan')
        ],
        states={
            ENTRY_PASSWORD_DECAN: [
                CallbackQueryHandler(handler_password, pattern=r'entry_password::[0-9]')
            ],
            COMPARE_PASSWORD_DECAN: [
                MessageHandler(Filters.text, handler_compare_password)
            ]
        },
        fallbacks=[CommandHandler('start', start)],
    )
)

dispatcher.add_handler(
    ConversationHandler(
        entry_points=[
            CallbackQueryHandler(handler_write_message, pattern=r'send_message::[0-9]')
        ],
        states={
            ENTRY_MESSAGE_DECAN: [
                MessageHandler(Filters.text, handler_send_message_students)
            ]
        },
        fallbacks=[CommandHandler('start', start)]
    )
)
