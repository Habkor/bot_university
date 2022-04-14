from django.core.management import BaseCommand
from django_bot.app_bot.main import run_bot


class Command(BaseCommand):
    """Команда для запуска пулинга телеграм бота."""

    help = "Запуск пулинга телеграм бота"  # noqa

    def handle(self, *args, **options):
        """Запуск пулинга телеграм бота."""
        run_bot()
