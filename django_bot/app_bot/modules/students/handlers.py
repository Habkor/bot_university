from django_bot.students.models import Student
from django_bot.core.bot import redis
from telegram.ext import CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler
from django_bot.core.bot import dispatcher
from telegram.ext import Filters
from django_bot.app_bot.modules.common.handlers import start
from django_bot.app_bot.keyboards.students.groups import get_groups_keyboard
from django_bot.groups.models import Group


STUDENT_NAME, STUDENT_SURNAME, STUDENT_PATRONYMIC, STUDENT_GROUP, END_DIALOG_STUDENT = range(5)


def register_student_name(update, _):
    """Регистрация студента с именем."""
    update.effective_message.reply_text('Введите ваше имя')
    return STUDENT_SURNAME


def register_student_surname(update, _):
    """Регистрация студента с фамилией."""
    redis.set(f'{update.effective_message.from_user.id}::name', update.message.text)
    update.effective_message.reply_text("Введите ваше фамилию")

    return STUDENT_PATRONYMIC


def register_student_patronymic(update, _):
    """Регистрация студента с отчества."""
    redis.set(f'{update.effective_message.from_user.id}::surname', update.message.text)
    update.effective_message.reply_text('Введите ваше отчество')

    return STUDENT_GROUP


def register_student_group(update, _):
    """Регистрация группы студента"""
    redis.set(f'{update.effective_message.from_user.id}::patronymic', update.message.text)

    update.effective_message.reply_text(
        'Выберите вашу группу',
        reply_markup=get_groups_keyboard()
    )

    return END_DIALOG_STUDENT


def register_student_end(update, _):
    """Регистрация группы и остальных данных."""

    name = redis.get(f'{update.callback_query.from_user.id}::name').decode("utf-8")
    surname = redis.get(f'{update.callback_query.from_user.id}::surname').decode("utf-8")
    patronymic = redis.get(f'{update.callback_query.from_user.id}::patronymic').decode("utf-8")
    group = update.callback_query.data.split('::')[1]

    group = Group.objects.filter(
        group_name=group
    ).first()

    student = Student()
    student.name = name
    student.surname = surname
    student.patronymic = patronymic
    student.group = group
    student.chat_id = update.effective_message.chat.id
    student.save()

    update.effective_message.reply_text('Спасибо за регистрацию')

    return ConversationHandler.END


dispatcher.add_handler(
    ConversationHandler(
        entry_points=[
            CallbackQueryHandler(register_student_name, pattern='student')
        ],
        states={
            STUDENT_SURNAME: [
                MessageHandler(filters=Filters.text, callback=register_student_surname)
            ],
            STUDENT_PATRONYMIC: [
                MessageHandler(filters=Filters.text, callback=register_student_patronymic)
            ],
            STUDENT_GROUP: [
                MessageHandler(filters=Filters.text, callback=register_student_group)
            ],
            END_DIALOG_STUDENT: [
                CallbackQueryHandler(register_student_end, pattern=r'group::[А-я][-\w]+[0-9]'),
            ],
        },
        fallbacks=[CommandHandler('start', start)]
    )
)
