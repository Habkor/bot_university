from django_bot.app_bot.modules.common.handlers import start
from django_bot.core.bot import redis, dispatcher
from telegram.ext import ConversationHandler, CallbackQueryHandler, MessageHandler, Filters, CommandHandler
from django_bot.app_bot.keyboards.students.groups import get_groups_keyboard
from django_bot.groups.models import Group
from django_bot.app_bot.keyboards.students.faculties import get_all_faculties
from django_bot.students.models import Student
from django_bot.app_bot.keyboards.schedules.schedules import get_button_schedule_keyboard


STUDENT_NAME, STUDENT_SURNAME, STUDENT_PATRONYMIC, FACULTY_STUDENT, STUDENT_GROUP, END_DIALOG_STUDENT = range(6)


def register_student_name(update, _):
    """Регистрация студента с именем."""
    student = Student.objects.filter(
        chat_id=update.effective_chat.id
    ).first()

    if not student:
        update.effective_message.reply_text('Введите ваше имя')
    else:
        update.effective_message.reply_text(
            'Посмотреть рассписание',
            reply_markup=get_button_schedule_keyboard()
        )
        return ConversationHandler.END

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

    return FACULTY_STUDENT


def register_student_faculty(update, _):
    """Регистрация факультета студента."""
    redis.set(f'{update.effective_message.from_user.id}::patronymic', update.message.text)

    update.effective_message.reply_text(
        "Выберите ваш факультет",
        reply_markup=get_all_faculties()
    )

    return STUDENT_GROUP


def register_student_group(update, _):
    """Регистрация группы студента"""
    faculty_name = update.callback_query.data.split('::')[1]

    update.effective_message.reply_text(
        'Выберите вашу группу',
        reply_markup=get_groups_keyboard(faculty_name)
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
            FACULTY_STUDENT: [
                MessageHandler(filters=Filters.text, callback=register_student_faculty)
            ],
            STUDENT_GROUP: [
                CallbackQueryHandler(register_student_group, pattern=r'faculty::[А-я]+')
            ],
            END_DIALOG_STUDENT: [
                CallbackQueryHandler(register_student_end, pattern=r'group::[А-я][-\w]+[0-9]'),
            ],
        },
        fallbacks=[CommandHandler('start', start)]
    )
)
