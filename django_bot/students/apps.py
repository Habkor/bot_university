from django.apps import AppConfig


class StudentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_bot.students'
    verbose_name = 'Студент'
    verbose_name_plural = 'Студенты'
