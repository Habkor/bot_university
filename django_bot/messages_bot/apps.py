from django.apps import AppConfig


class MessagesBotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_bot.messages_bot'
    verbose_name = 'Сообщение'
    verbose_name_plural = 'Сообщения'
