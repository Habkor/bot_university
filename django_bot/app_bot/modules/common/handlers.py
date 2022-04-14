from django_bot.core.bot import updater
from django_bot.app_bot.keyboards.common.start import get_start_keyboard
from telegram.ext import CommandHandler


def start(update, _):
    update.message.reply_text('Добро пожаловать! Кем вы являетесь в вузе?', reply_markup=get_start_keyboard())


updater.dispatcher.add_handler(CommandHandler('start', start))
