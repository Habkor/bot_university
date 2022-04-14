from django_bot.core.bot import updater
from django_bot.core.load import load_modules
import logging


def run_bot():
    """Функция, которая запускает бота."""
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO
    )

    load_modules()
    updater.start_polling()
