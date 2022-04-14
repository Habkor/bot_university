from django_bot.core.bot import dispatcher
from telegram.ext import CallbackQueryHandler


def handler_password(update, context):
    """Эта функция срабатывается после нажатия деканаом кнопки отправить пароль."""
    print("Вы нажали кнопку ввести пароль")


dispatcher.add_handler(
    CallbackQueryHandler(handler_password, pattern="^decan::[0-9]")
)
